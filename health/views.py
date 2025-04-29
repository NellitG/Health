from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.shortcuts import render
from rest_framework import viewsets
from .models import Client, Program, Enrollment
from .serializer import ClientSerializer, ProgramSerializer, EnrollmentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .serializer import ClientProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import ClientDocument
from .serializer import ClientDocumentSerializer

# Create your views here.
class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientProfileSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    filterset_fields = ['first_name', 'last_name', 'gender'] 
    ordering_fields = ['first_name', 'last_name, date_of_birth']
    ordering = ['first_name']
    search_fields = ['first_name', 'last_name']

    @action(detail=True, methods=['get'])
    def profile(self, request, pk=None):
        client = self.get_object()
        serializer = ClientProfileSerializer(client)
        return Response(serializer.data)
    
class ClientDocumentViewSet(viewsets.ModelViewSet):
    queryset = ClientDocument.objects.all()
    serializer_class = ClientDocumentSerializer
    parser_classes = (MultiPartParser, FormParser)

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
