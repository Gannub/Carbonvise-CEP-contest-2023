from django.db import models
from django.urls import reverse
from profiles.utils import check_slug_unique
from django.db.models.signals import pre_save, post_save
from django.contrib.auth import get_user_model
from profiles.models import CreditSession, CreditHistory

User = get_user_model()


def upload_path(instance, filename):
    return f'badges/{instance}/{filename}'


class NeutralBadges(models.Model): 
        in_session = models.OneToOneField(CreditSession,related_name='badges',on_delete=models.DO_NOTHING)
        session_name = models.CharField(max_length=100, null=True, blank=True)
        slug = models.SlugField(unique=True,null=True,blank=True)
        badges = models.ImageField(null=True,blank=True, upload_to = upload_path)
        is_obtained = models.BooleanField(default=False)


def upload_path_archive(instance, filename):
    return f'badges_archive/{instance}/{filename}'

class ArchiveNeutralBadge(models.Model):
        in_session = models.OneToOneField(CreditHistory,related_name='badges',on_delete=models.CASCADE)
        name = models.CharField(max_length=100, null=True, blank=True)
        slug = models.SlugField(unique=True,null=True,blank=True)
        badges = models.ImageField(null=True,blank=True, upload_to = upload_path_archive)





       