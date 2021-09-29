from django.db import models

Houses = [
    ('Aryabhata', 'Aryabhata'),
    ('Ashoka', 'Ashoka'),
    ('Buddha', 'Buddha'),
    ('Chanakya', 'Chanakya'),
]
# Create your models here.
class StudentDetail(models.Model):
    Name = models.CharField(default="",verbose_name="Student Name",max_length=119)
    House = models.CharField(default="",verbose_name="Student House",choices=Houses,max_length=119)
    Bus = models.CharField(default="D-",verbose_name="Student Bus No.",max_length=119)
    DOB = models.DateField(default="",verbose_name="Student DOB")
    def __str__(self):
        return f"Name: {self.Name[0:15]}, House: {self.House}, Bus: {self.Bus} and DOB: {self.DOB}"