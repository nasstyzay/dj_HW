from rest_framework import viewsets
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .permissions import IsAuthorOrReadOnly, CanCreateAdvertisement

class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthorOrReadOnly, CanCreateAdvertisement]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthorOrReadOnly, CanCreateAdvertisement]
        elif self.action == 'list':
            self.permission_classes = []
        return super().get_permissions()
