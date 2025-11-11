from django.urls import path
from .views import LoginView, RegisterView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
]