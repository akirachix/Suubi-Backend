from django.db import models
from members.models import Member

class Loan(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='loan')
    loan_number = models.CharField(max_length=20, unique=True)
    loan_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    term = models.PositiveIntegerField()  # in months
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[
    ('applied', 'Applied'),
    ('approved', 'Approved'),
    ('disbursed', 'Disbursed'),
    ('repaying', 'Repaying'),
    ('completed', 'Completed'),
    ('rejected', 'Rejected')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.member_id.name} - {self.loan_number}"