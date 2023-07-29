from django.contrib import admin

# Register your models here.
from profiles.models import Profile, CreditSession, CreditHistory, Achievement


admin.site.register(Profile)
admin.site.register(CreditSession)  
admin.site.register(CreditHistory)  
admin.site.register(Achievement)  