"""peladasApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function:p from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import refresh_jwt_token,obtain_jwt_token
from players.views import PeladaViewSet, PeladaDetailViewSet, ConfiguracaoDetailViewSet, PeladaListUser
from users import views as views_user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-refresh/',obtain_jwt_token),
    path('auth/',include('rest_framework_social_oauth2.urls')),
    path('api/peladas/', PeladaViewSet.as_view()),
    path('api/user-peladas/', PeladaListUser.as_view()),
    path('api/peladas/<int:pk>', PeladaDetailViewSet.as_view(), name='pelada-detail'),
    path('api/configuracao/<int:pk>', ConfiguracaoDetailViewSet.as_view(), name='configuracao-detail'),
    path('api/user/<int:pk>', views_user.UserDetailViewSet.as_view(), name='user-detail')
]
