from django.contrib import admin
from django.urls import include, path
from polls import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("polls/", include("polls.urls")),
    path('', views.home, name='home'),
    path("admin/", admin.site.urls),
    path('login/', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]