#from django.contrib import admin
from django.urls import path
from media import views
urlpatterns = [
    path('file-upload/' , views.upload_file , name='file')
   
]