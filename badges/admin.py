from django.contrib import admin

# Register your models here.
from .models import NeutralBadges, ArchiveNeutralBadge


admin.site.register(NeutralBadges)
admin.site.register(ArchiveNeutralBadge)