from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=40)
    mobile=models.CharField(max_length=10)
    email=models.EmailField()
    address=models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Conatact(models.Model):
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.CharField(max_length=255)


    def __str__(self):
        return self.email