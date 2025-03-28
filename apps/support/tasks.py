from celery import shared_task
from datetime import timedelta, datetime
from .models import SupportTicket

@shared_task
def auto_close_old_tickets():
    cutoff = datetime.now() - timedelta(days=30)
    closed = SupportTicket.objects.filter(status='in_progress', created_at__lt=cutoff)
    count = closed.update(status='closed')
    return f"Auto-closed {count} stale tickets"
