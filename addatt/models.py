from django.db import models

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document

class Attcsv(models.Model):
    pass
    Time = models.CharField(max_length=255, blank=True)
    User_full_name = models.CharField(max_length=255, blank=True)
    Affected_user = models.CharField(max_length=255, blank=True)
    Event_context = models.CharField(max_length=255, blank=True)
    Component = models.CharField(max_length=255, blank=True)
    Event_name = models.CharField(max_length=255, blank=True)
    Description = models.CharField(max_length=255, blank=True)
    Origin = models.CharField(max_length=255, blank=True)
    IP_address = models.CharField(max_length=255, blank=True) 


    def __str__(self):
        return self.User_full_name


class Contact(models.Model):
    first_name= models.CharField(max_length=50 , blank=True, null=True)
    last_name= models.CharField(max_length=50 , blank=True, null=True)
    email= models.EmailField()
    ip_address= models.CharField(max_length=50 , blank=True, null=True)
    message= models.TextField()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

""" for more details please check this website
https://medium.com/@simathapa111/how-to-upload-a-csv-file-in-django-3a0d6295f624 """


