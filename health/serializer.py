from rest_framework import serializers
from .models import Client, Program, Enrollment

# Define the serializer for the Program model
class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['id', 'name', 'description']

# Define the serializer for the Client model
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

# Define the serializer for the Enrollment model
class EnrollmentSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    program = serializers.PrimaryKeyRelatedField(queryset=Program.objects.all())

    class Meta:
        model = Enrollment
        fields = '__all__'

# Define a profile serializer that includes a list of enrolled programs
class ClientProfileSerializer(serializers.ModelSerializer):
    programs = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'programs']

    def get_programs(self, obj):
        return ProgramSerializer(
            [Enrollment.program for Enrollment in obj.enrollments.all()],
            many=True
        ).data
