from celery import shared_task
from datetime import date
from .models import Subscription

@shared_task
def deactivate_expired_subscriptions():
    today = date.today()
    expired = Subscription.objects.filter(end_date__lt=today, is_active=True)
    count = expired.update(is_active=False)
    return f"Deactivated {count} expired subscriptions"
