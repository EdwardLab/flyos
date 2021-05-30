
from django.urls import path
 
from . import views
# urls.py

from functools import partial
from django.urls import path
from django.views.static import serve
from pywebio import STATIC_PATH
from pywebio.platform.django import webio_view
webio_view_func = webio_view

  


from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r"panel", webio_view_func),
    path('', views.panel),
]
