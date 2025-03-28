from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class EnergyUsage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    energy_consumed_kwh = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.date}"
