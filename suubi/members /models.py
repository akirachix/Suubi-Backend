from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    member_id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    start_date = models.DateField()
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"{self.name} {self.photo}, {self.member_id}"