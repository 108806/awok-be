"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from products.views import api_home, example_view

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken import views

from products.views import UserDetailAPI,RegisterUserAPIView, UsersDetailAPI, ChangePasswordView, DeleteUserAPI, SessionViewAPI, UserUpdateView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    ...

]

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
)

urlpatterns = [
    path("admin", admin.site.urls),
    #path('api', api_home),
    #path('test', example_view),
    #path('api-token-auth', views.obtain_auth_token),
    #path('get-user-by-id', UserDetailAPI.as_view()),
    
    path('<int:pk>', UserDetailAPI.as_view()),
    path('api/register',RegisterUserAPIView.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/get-user', UserDetailAPI.as_view()),
    path('api/get-users', UsersDetailAPI.as_view()),
    path('api/delete-user', DeleteUserAPI),
    path('api/change-password', ChangePasswordView.as_view()),
    
    path('api/get-session', SessionViewAPI.as_view()),

    path('api/get-token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/user-update', UserUpdateView.as_view()),
    
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

