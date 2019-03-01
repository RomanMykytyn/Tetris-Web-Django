from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('signIn/', views.signIn),
    path('exitAcc/', views.exitAcc),
    #path('signUp/', views.signUp),

]
