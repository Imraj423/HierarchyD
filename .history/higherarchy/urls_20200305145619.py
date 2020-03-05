"""higherarchy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from dropbox.views import tree_view, login_view, register_user_view, logout_view, new_file_view
from mptt.admin import DraggableMPTTAdmin

from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_files, name='home'),
    path('newfile/', views.new_file_view, name='newfile'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name="loginview"),
    path('register/', register_user_view, name="registerview"),
]


