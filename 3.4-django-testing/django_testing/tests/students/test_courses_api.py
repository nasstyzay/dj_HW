import pytest
from model_bakery import baker
from django.urls import reverse
from rest_framework.test import APIClient
from students.models import Course, Student

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def course_factory():
    def factory(**kwargs):
        return baker.make(Course, **kwargs)
    return factory

@pytest.fixture
def student_factory():
    def factory(**kwargs):
        return baker.make(Student, **kwargs)
    return factory

@pytest.mark.django_db
def test_retrieve_course(api_client, course_factory):
    course = course_factory()
    url = reverse('course-detail', args=[course.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data['id'] == course.id

@pytest.mark.django_db
def test_list_courses(api_client, course_factory):
    courses = course_factory(_quantity=3)
    url = reverse('course-list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 3

@pytest.mark.django_db
def test_filter_courses_by_id(api_client, course_factory):
    course1 = course_factory()
    course2 = course_factory()
    url = reverse('course-list') + f'?id={course1.id}'
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['id'] == course1.id

@pytest.mark.django_db
def test_filter_courses_by_name(api_client, course_factory):
    course1 = course_factory(name='Course A')
    course2 = course_factory(name='Course B')
    url = reverse('course-list') + '?name=Course A'
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == 'Course A'

@pytest.mark.django_db
def test_create_course(api_client):
    url = reverse('course-list')
    data = {'name': 'New Course'}
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    assert response.data['name'] == 'New Course'

@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    course = course_factory()
    url = reverse('course-detail', args=[course.id])
    data = {'name': 'Updated Course'}
    response = api_client.put(url, data, format='json')
    assert response.status_code == 200
    assert response.data['name'] == 'Updated Course'

@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    course = course_factory()
    url = reverse('course-detail', args=[course.id])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert not Course.objects.filter(id=course.id).exists()
