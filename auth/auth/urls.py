# project_name/urls.py

from django.contrib import admin
from django.urls import path
from auth.views import login_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]
