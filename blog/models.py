from django.db import models

# Create your models here.
class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    slug=models.CharField(max_length=200)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=100)
    query=models.TextField()

    def __str__(self):
        return self.name

class Member(models.Model):
    user_name=models.CharField(max_length=40)
    pwd=models.CharField(max_length=25)
    email=models.CharField(max_length=40)
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)

    def __str__(self):
        return self.first_name+" "+self.last_name
    