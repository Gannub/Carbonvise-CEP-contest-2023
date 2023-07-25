from django.contrib import admin

# Register your models here.
from profiles.models import Profile, CreditSession, CreditHistory


admin.site.register(Profile)
admin.site.register(CreditSession)  
admin.site.register(CreditHistory)  