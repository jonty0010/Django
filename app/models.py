from django.db import models

# Create your models here.
class Student(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact = models.BigIntegerField()
    
    def __str__(self):
        return self.fname