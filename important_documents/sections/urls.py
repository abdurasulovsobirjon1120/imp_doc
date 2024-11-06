from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SectionListCreateView, DocumentUploadView, DocumentUpdateView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sections/', SectionListCreateView.as_view(), name='section-list-create'),
    path('<int:section_id>/files/', DocumentUploadView.as_view(), name='document-upload'),
    path('files/<int:pk>/', DocumentUpdateView.as_view(), name='document-update'),
]
