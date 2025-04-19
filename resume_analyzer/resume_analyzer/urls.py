"""
URL configuration for resume_analyzer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from users.views import RegisterView, verify_email, PasswordResetView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.utils import send_password_reset_email
from users.views import get_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', get_user),
    path('api/register/', RegisterView.as_view()),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/verify-email/<uidb64>/<token>/', verify_email, name = 'verify_email'),
    path('api/password-reset/', send_password_reset_email, name = 'password_reset'),
    path('api/password-reset-confirm/<uidb64>/<token>/', PasswordResetView.as_view(), name = 'password-reset-confirm'),
    path('api/resumes/', include('resumes.urls')),
]

