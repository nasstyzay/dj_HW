from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer

class SensorCreateView(generics.CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorUpdateView(generics.UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorListView(generics.ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorDetailView(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasurementCreateView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
