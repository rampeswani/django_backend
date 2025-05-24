#from django.contrib import admin
from django.urls import path
from LoginUtility import views
urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('get-user',views.get_current_user,name = 'current-user')
]