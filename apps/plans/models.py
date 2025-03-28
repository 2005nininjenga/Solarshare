from django.db import models

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    duration_months = models.PositiveIntegerField(default=1)  # e.g., 1 = monthly
    limit_kwh = models.FloatField(help_text="Max energy allowed per month (kWh)")
    overuse_charge_per_kwh = models.DecimalField(max_digits=6, decimal_places=2, help_text="Charge per kWh over the limit")
    features = models.TextField(blank=True, help_text="Comma-separated features")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} – Ksh {self.price_per_month}/mo"
