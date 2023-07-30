from django.db import models
from django.urls import reverse
from profiles.utils import check_slug_unique
from django.db.models.signals import pre_save, post_save
from django.contrib.auth import get_user_model
from profiles.models import CreditSession, CreditHistory , Achievement

User = get_user_model()


def upload_path(instance, filename):
    return f'badges/{instance}/{filename}'
def ach_upload_path(instance, filename):
    return f'ach_badges/{instance}/{filename}'

class NeutralBadges(models.Model): 
        in_session = models.OneToOneField(CreditSession,related_name='badges',on_delete=models.SET_NULL,null=True)
        session_name = models.CharField(max_length=100, null=True, blank=True)
        slug = models.SlugField(unique=True,null=True,blank=True)
        badges = models.ImageField(null=True,blank=True, upload_to = upload_path)
        is_obtained = models.BooleanField(default=False)

        def __str__(self) -> str:
            return f'{self.in_session} {self.is_obtained}'
        
class AchievementBadges(models.Model):
        in_session = models.ForeignKey(CreditSession, related_name='ach_badge', on_delete=models.SET_NULL, null=True)
        in_achievement = models.ForeignKey(Achievement, related_name='in_achievement', on_delete=models.SET_NULL, null=True)
        session_name = models.CharField(max_length=100, null=True, blank=True)
        slug = models.SlugField(unique=True,null=True,blank=True)
        badges = models.ImageField(null=True,blank=True, upload_to = ach_upload_path)
        is_obtained = models.BooleanField(default=False)

        def __str__(self) -> str:
            return f'{self.in_session} {self.in_achievement} {self.is_obtained}'
        
def pre_save_slug_field(sender, instance, *arg ,**kwargs):  # sent at the beginning of a model’s save() 
        if not instance.slug:
            instance.slug = check_slug_unique(instance)

pre_save.connect(pre_save_slug_field, sender=AchievementBadges)

def upload_path_archive(instance, filename):
    return f'badges_archive/{instance}/{filename}'

class ArchiveNeutralBadge(models.Model):
        in_session = models.OneToOneField(CreditHistory,related_name='badges',on_delete=models.CASCADE)
        name = models.CharField(max_length=100, null=True, blank=True)
        slug = models.SlugField(unique=True,null=True,blank=True)
        badges = models.ImageField(null=True,blank=True, upload_to = upload_path_archive)





       