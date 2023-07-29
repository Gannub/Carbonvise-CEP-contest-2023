from django.contrib import admin

# Register your models here.
from .models import NeutralBadges, ArchiveNeutralBadge ,AchievementBadges


admin.site.register(NeutralBadges)
admin.site.register(ArchiveNeutralBadge)

admin.site.register(AchievementBadges)