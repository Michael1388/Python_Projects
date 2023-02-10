from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from .import views



urlpatterns = [
    #path('',views.home, name="home"),
    #path('admin/', admin.site.urls),
    #path('', include('profiles.urls')),

    path('profiles', views.profiles, name="profiles"),
    path('<int:pk>/details/', views.details, name="details"),
]