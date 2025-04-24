from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProgramViewSet, ClientViewSet, EnrollmentViewSet

router = DefaultRouter()
router.register(r'program', ProgramViewSet)
router.register(r'client', ClientViewSet)
router.register(r'enrollment', EnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]