from django.db import models

from profiles.utils import check_slug_unique
from django.db.models.signals import pre_save, post_save
from django.contrib.auth import get_user_model

# from market.models import Market
    
User = get_user_model()
#seperate calls to avoid circular import.
# class User(AbstractUser):
#     pass

class Profile(models.Model):
    #remind about dealer 
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    about_dealer = models.TextField(null=True,blank=True)
    slug = models.SlugField(unique=True,null=True,blank=True)
    
    def __str__(self):
        return f'{self.user.username}'
    
def pre_save_slug_field(sender, instance, *arg ,**kwargs):  # sent at the beginning of a model’s save() 
    if not instance.slug:
        instance.slug = check_slug_unique(instance)
pre_save.connect(pre_save_slug_field, sender=Profile)

def post_save_profile_create(sender ,instance, created, *arg, **kwargs): # sent at the end of the save()
    if created:
        Profile.objects.create(user=instance)
post_save.connect(post_save_profile_create, sender=User)
