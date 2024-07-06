from django.db import models
from members.models import Member

# Create your models here.

class Accounts(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='account')
    account_number = models.CharField(max_length=20, unique=True)
    account_type = models.CharField(max_length=20, choices=[
        ('savings', 'Savings'),
    ('shares', 'Shares')
    ])
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.account_number}'