from django.urls import path, re_path
from auth_app import views

app_name = "auth_app"

urlpatterns = [
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'logout/$', views.user_logout, name='logout'),
    re_path(r'^special/$', views.special, name='special'),
    re_path(r'^login/$', views.user_login, name='login')
]