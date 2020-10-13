from django.urls import path, include
from . views import homepage, upload, contact_upload,contact_upload2

app_name='addatt'
urlpatterns = [
    path('',homepage, name="homepage"),
    path('upload/',upload, name="upload"),  
    path('upload-csv/', contact_upload, name="contact_upload"),
     path('upload-csv2/', contact_upload2, name="contact_upload2")
]