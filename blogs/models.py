from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from blogs.utils import check_slug_unique
from django.db.models.signals import pre_save, post_save

User = get_user_model()
# Create your models here.

Blog_Category = (
                 ('1','Top Posts'),
                 ('2','Tips'),
                 ('3','News'),
                 ('4','Events')
)

def upload_path(instance, filename):
    return f'profiles/{instance}/{filename}'

# class Author(models.Model):
#     name = models.OneToOneField(User, on_delete=models.CASCADE)
#     slug = models.SlugField(unique=True,null=True,blank=True)
#     profile_picture = models.ImageField(null=True,blank=True)

#     def __str__(self) :
#         return self.user.username
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    slug = models.SlugField(unique=True,null=True,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.CharField(max_length=100, choices=Blog_Category, null=True, blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self) :
        return self.title
    
    def get_absolute_url(self):
        return reverse('blogs:post_detail', kwargs={
            'slug': self.slug
    })
    
    @property
    def get_comments(self):
        return self.comments.all()
    
    @property
    def get_province_name(self):
        for cat in Blog_Category:
            if self.categories == cat[0]:
                return cat[1]
    

    
def pre_save_slug_field(sender, instance, *arg ,**kwargs):  # sent at the beginning of a model’s save() 
        if not instance.slug:
            instance.slug = check_slug_unique(instance)

pre_save.connect(pre_save_slug_field, sender=Post)



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(Post,related_name='comments' , on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
