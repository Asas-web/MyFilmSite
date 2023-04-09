from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('register', views.registeruser,name='register'), 
    path('login', views.loginuser,name='login'),	
    path('homepage', views.homepage,name='homepage'), 
    path('addfilm', views.addfilm,name='addfilm'), 
    path('log_out', views.log_out,name='log_out'), 
    path('addnewfilm', views.addnewfilm,name='addnewfilm'),
    path('showfilm/<int:pk>/', views.showfilm, name='showfilm'),
    path('deletefilm/<int:pk>/', views.deletefilm, name='deletefilm'),
    path('editfilm/<int:pk>/', views.editfilm, name='editfilm'),
    path('editfilm/<int:pk>/makeedit', views.makeedit, name='makeedit'),

]