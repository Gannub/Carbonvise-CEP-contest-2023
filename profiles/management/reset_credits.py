from django.core.management.base import BaseCommand
from django.utils import timezone
from profiles.models import CreditSession ,CreditHistory

class Command(BaseCommand):
    help = 'Reset user purchased credits every month'

    def handle_(self, *args, **kwargs):
        # Get the current date and the first day of the next month
        # now = timezone.now()

        # next_month = now.replace(day=1) + timezone.timedelta(days=32)
        # next_month = next_month.replace(day=1)

        # Reset credits for all users whose last purchase date was before the next month
        # (20jul :: admins have to run the commands periodically)
        # I should try to add schedule or cron??
        CreditSession.objects.all().update(session_active=False)


# print(timezone.now())