"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls as auth_urls
from django.views.generic import TemplateView

from Blog import settings
from News.views import index as news_index
from Partner.views import index as partner_index
from Auth.views import SignUpView

urlpatterns = [
    path('', news_index, name='news_index'),
    path('admin/', admin.site.urls),
    path('user/', include(auth_urls)),
    path('user/register/', SignUpView.as_view(), name='register'),
    path('partners/', partner_index, name='partner_index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
