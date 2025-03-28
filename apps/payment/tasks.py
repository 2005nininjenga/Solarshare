from celery import shared_task
from .models import Payment

@shared_task
def process_payment(payment_id):
    try:
        payment = Payment.objects.get(id=payment_id)
        payment.status = 'success'  # You can simulate logic here
        payment.save()
        return f"Payment {payment.reference} processed"
    except Payment.DoesNotExist:
        return f"Payment ID {payment_id} not found"
