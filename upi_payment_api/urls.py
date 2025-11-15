"""
URL configuration for upi_payment_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.management import call_command
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def migrate_view(request):
    try:
        call_command("makemigrations")
        call_command("migrate")
        return JsonResponse({"message": "Migrations applied successfully"})
    except Exception as e:
        return JsonResponse({"error": str(e)})

def create_admin(request):
    """
    Temporary route to create a superuser on Render deployment.
    Remove after first login.
    """
    try:
        if User.objects.filter(username="subha").exists():
            return JsonResponse({"message": "Admin already exists"})

        User.objects.create_superuser(
            username="subha",
            email="",
            password="Subha@2003"
        )
        return JsonResponse({"message": "Admin created successfully"})

    except Exception as e:
        return JsonResponse({"error": str(e)})


urlpatterns = [
    # Redirect root `/` → admin
    #path('', admin.site.urls),
    path('', lambda request: JsonResponse({"status": "UPI Payment API is running"})),

    # Django Admin
    path('admin/', admin.site.urls),

    # TEMPORARY ADMIN CREATION ROUTE
    path("migrate/", migrate_view),
    path("create-admin/", create_admin),

    # API routes
    path('api/auth/', include('auth.urls')),
    path('api/payments/', include('payments.urls')),

    # JWT Auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Webhooks
    path('api/webhooks/', include('webhooks.urls')),
]
