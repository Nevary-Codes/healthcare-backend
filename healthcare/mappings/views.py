from rest_framework import viewsets
from .models import PatientDoctorMapping
from .serializers import MappingSerializer
from rest_framework.permissions import IsAuthenticated

class MappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [IsAuthenticated]