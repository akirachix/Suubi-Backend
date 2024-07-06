from django.db import models
from members.models import Member 

# Create your models here.
class MilkSales(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='milk_sales')
    litres = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_date = models.DateField()
    price_per_litre = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.member_id} {self.litres}"