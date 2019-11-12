"""portfolio_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name = "job_home"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# So this line says, hey... whenever you are adding static files, we want to have
# media URL and media ROOt. In short, this is where you look for the information
# The media url is stored in settings.py "MEDIA_URL = '/media/'"
