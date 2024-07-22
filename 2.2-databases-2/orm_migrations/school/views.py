from django.views.generic import ListView
from django.shortcuts import render

from .models import Student

def student_list(request):
    students = Student.objects.prefetch_related('teachers')
    return render(request, 'template.html', {'students': students})
