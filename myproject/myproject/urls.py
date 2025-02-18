"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
# from django.conf import settings
# from django.conf.urls.static import static
# from myproject.lection3.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('ti/', include('seminar_3.urls')),
    # path('wy/', include('myapp.urls')),
    # path('wm/', include('wmodel.urls')),
    path('lec/', include('lection3.urls')),
    # path('', index),
    path('f/', include('lec_forms.urls')),
    path('fs/', include('form_seminar.urls')),
    path('hw/', include('hw_logik_and_template.urls')),
    path('__debug__/', include("debug_toolbar.urls")),
]
