from django.db import models
from members.models import Members

class Loans(models.Model):
    member_id = models.ForeignKey(Members, on_delete=models.CASCADE,related_name='loans')
    loan_number = models.SmallIntegerField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    term = models.CharField(max_length=6, choices=[('Short','Short'), ('medium','medium'), ('long','long')])
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=[('applied', 'Applied'),('approved', 'Approved'),('completed', 'Completed')])
    created_on = models.DateField(auto_now_add =True)
    updated_on = models.DateField(auto_now=True)

def __str__(self):
    return f'{self.loan_number}'


#  Create your models here.
