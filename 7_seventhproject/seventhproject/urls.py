"""seventhproject URL Configuration

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
from django.contrib import admin
from django.urls import path
import crud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crud.views.index, name="index"),
    path('new/', crud.views.new, name="new"),
    path('create/', crud.views.create, name="create"),
    path('read/<int:post_id>', crud.views.read, name="read"),
    path('update/<int:post_id>', crud.views.update, name="update"),
    path('update_page/<int:post_id>', crud.views.update_page, name="update_page"),
    path('delete/<int:post_id>', crud.views.delete, name="delete"),
]
