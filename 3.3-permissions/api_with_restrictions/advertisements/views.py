from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend, DateFromToRangeFilter
from .models import Advertisement
from .serializers import AdvertisementSerializer
from rest_framework.exceptions import PermissionDenied


class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created_at', 'status']
    filterset_class = DateFromToRangeFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied("You cannot update this advertisement")
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("You cannot delete this advertisement")
        super().perform_destroy(instance)
