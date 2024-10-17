"""AIMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from user_functions import views
from django.conf.urls import url, include


urlpatterns = [
    path('', views.landing, name='landing'),
    path('user_functions/', include('user_functions.urls')),
    path('scopes/', include('scopes.urls')),
    path('projects/', include('projects.urls')),
    path('reports/', include('reports.urls')),
    path('admin/', admin.site.urls),
    url(r'^advanced_filters/', include('advanced_filters.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
