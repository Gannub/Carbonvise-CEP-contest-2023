from django.db import models
from django.contrib.auth.models import AbstractUser
# from dealer.models import Dealer
# Create your models here.


class User(AbstractUser):
    is_dealer = models.BooleanField(default=False)
    # dealer = models.OneToOneField(Dealer,)
    def make_dealer(self):
        self.is_dealer =True
        self.save()
