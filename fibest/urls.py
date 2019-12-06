"""fibest URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from fibest.views import index
from fibest.views import login
from fibest.views import dashboard
from fibest.views import inscription
from fibest.views import magazine
from fibest.views import forum
from fibest.views import stand


urlpatterns = [
                  url(r'^tinymce/', include('tinymce.urls')),
                  path('admin/', admin.site.urls),
                  path('', index.index, name='index'),
                  path('login/', login.login, name="login"),
                  path('dashboard/', dashboard.index, name="dashboard"),
                  path('inscription/', inscription.index, name="inscription"),
                  path('magazine/', magazine.index, name="magazine"),
                  path('stand/', stand.index, name="stand"),
                  path('forum/', forum.index, name="forum")
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
