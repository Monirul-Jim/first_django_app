from django.db import models

# Create your models here.


class Teacher(models.Model):
    tid = models.IntegerField()
    tName = models.CharField(max_length=40)
    tEmail = models.EmailField(max_length=30)
