from celery import shared_task
from django.contrib.auth import get_user_model
from .models import Notification

@shared_task
def send_notification(user_id, message):
    User = get_user_model()
    try:
        user = User.objects.get(id=user_id)
        Notification.objects.create(user=user, message=message)
        return f"Sent notification to {user.username}"
    except User.DoesNotExist:
        return f"User ID {user_id} not found"
