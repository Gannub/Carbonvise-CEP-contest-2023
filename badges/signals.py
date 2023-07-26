from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from badges.models import NeutralBadges, ArchiveNeutralBadge
from profiles.models import CreditSession, CreditHistory
from django.urls import reverse
from django.test import RequestFactory
from badges.views import obtainBadges

# @receiver(post_save, sender=CreditSession)
# def give_badges(sender, instance, created, **kwargs):
#     if instance.is_neutral and created:
#         # triggers a function in views.py
#         print('test not passseddddd')
#         url = reverse('badges:')
#         # request = RequestFactory().get(url)

#         obtainBadges(request)
#         print('test passsssssssssssssssssssssss')
        
        