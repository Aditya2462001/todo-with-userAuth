from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    author = models.OneToOneField(User,on_delete=models.CASCADE)
    name   = models.CharField( max_length=50)
    lname  = models.CharField(max_length=50,blank=True,null=True)
    email  = models.CharField(max_length=50,blank=True,null=True)
    image  = models.ImageField(upload_to="profile_pic", blank=True , null = True)
    number = models.CharField(max_length = 10 ,blank=True,null=True)


    def __str__(self):
        return str(self.author)

class ToDo(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000,blank=True,null=True)
    date_time = models.DateTimeField( auto_now_add=True)
    done = models.BooleanField(default=False)


    def __str__(self):
        return self.content


    

