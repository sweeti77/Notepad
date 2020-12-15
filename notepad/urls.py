"""notepad URL Configuration

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

from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('homePage', views.homePage, name="homePage"),
    path('create_note', views.create_note, name="create_note"),
    path('updateNote/<int:note_pk>', views.update_note, name="update_note"),
    path('updateNote/<int:note_pk>/delete_note', views.delete_note, name="delete_note"),

    #Authentication URLS
    path('signup', views.signupUser, name="signupUser"),
    path('login', views.loginUser, name="loginUser"),
    path('logout', views.logoutUser, name="logoutUser"),

]
