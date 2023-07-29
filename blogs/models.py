from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from blogs.utils import check_slug_unique
from django.db.models.signals import pre_save, post_save

User = get_user_model()
# Create your models here.

def upload_path(instance, filename):
    return f'profiles/{instance}/{filename}'

class Author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True,)
    slug = models.SlugField(unique=True,null=True,blank=True)
    image = models.ImageField(null=True,blank=True, upload_to = upload_path)

    def __str__(self) :
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    slug = models.SlugField(unique=True,null=True,blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) :
        return self.title
