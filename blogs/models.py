from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from blogs.utils import check_slug_unique
from django.db.models.signals import pre_save, post_save

User = get_user_model()
# Create your models here.

Blog_Category = (('1','For you'),
                 ('2','Top Posts'),
                 ('3','Tips'),
                 ('4','News'),
                 ('5','Events')
)

def upload_path(instance, filename):
    return f'profiles/{instance}/{filename}'

class Author(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True,null=True,blank=True)
    profile_picture = models.ImageField(null=True,blank=True)

    def __str__(self) :
        return self.user.username
    
class Category(models.Model):
    title = models.CharField(max_length=100, choices=Blog_Category)
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    profile_picture = models.ImageField(null=True,blank=True)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    slug = models.SlugField(unique=True,null=True,blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self) :
        return self.title
    
def pre_save_slug_field(sender, instance, *arg ,**kwargs):  # sent at the beginning of a model’s save() 
        if not instance.slug:
            instance.slug = check_slug_unique(instance)

pre_save.connect(pre_save_slug_field, sender=Post)

def get_absolute_url(self):
    return reverse('post_detail', kwargs={
        'slug': self.slug
    })
