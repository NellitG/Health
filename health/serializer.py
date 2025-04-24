from rest_framework import serializers
from .models import Client, Program, Enrollment

#Define the serializer for the Program model
class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

#Define the serializer for the Client model
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
#To convert Enrollment model to JSON format
class EnrollmentSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    program = serializers.PrimaryKeyRelatedField(queryset=Program.objects.all())

    class Meta:
        model = Enrollment
        fields = '__all__'