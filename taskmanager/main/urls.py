from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('create', views.creator, name="create"),
    path('information', views.info, name="information"),
    path('sign-in', views.sign_in, name="sign-in"),
    path('log-in', views.log_in, name="log-in"),
]
