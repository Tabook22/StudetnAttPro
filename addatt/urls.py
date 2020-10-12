from django.urls import path, include
from . views import homepage, upload

app_name='addatt'
urlpatterns = [
    path('',homepage, name="homepage"),
    path('upload/',upload, name="upload"),   
]