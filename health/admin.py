from django.contrib import admin
from .models import Client, Program, Enrollment

# Register your models here.

#Register Program model
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

#Register Client model
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'date_of_birth', 'gender')
    search_fields = ('first_name', 'last_name')

#Register Enrollment model
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'program', 'enrolled_on')
    list_filter = ('program',)
    search_fields = ('client__first_name', 'program__name')
