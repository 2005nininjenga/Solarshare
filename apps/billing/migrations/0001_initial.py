# Generated by Django 5.1.7 on 2025-03-27 05:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plans', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('transaction_id', models.CharField(max_length=100, unique=True)),
                ('plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plans.subscriptionplan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
