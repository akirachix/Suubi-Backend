from django.db import models
from members.models import Members


class Accounts(models.Model):
    member_id = models.ForeignKey(Members, on_delete=models.CASCADE, related_name='account')
    account_number = models.CharField(max_length=20, unique=True)
    account_type = models.CharField(max_length=20, choices=[
        ('savings', 'Savings'),
    ('shares', 'Shares')
    ])
    balance = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
def __str__(self):
    return f'{self.balance}'

# 