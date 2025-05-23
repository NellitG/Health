from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProgramViewSet, ClientViewSet, EnrollmentViewSet, ClientDocumentViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



router = DefaultRouter()
router.register(r'program', ProgramViewSet)
router.register(r'client', ClientViewSet, basename='client')
router.register(r'enrollment', EnrollmentViewSet)
router.register(r'document', ClientDocumentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]