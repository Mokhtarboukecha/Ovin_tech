from django.db import models
from breeds.models import Breed
from datetime import date

class Sheep(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    PURCHASE_CHOICES = [('Born At Farm', 'Born At Farm'), ('Purchased', 'Purchased')]
    BIRTH_TYPE_CHOICES = [
        ('Single', 'Single'), ('Twin', 'Twin'),
        ('Triplet', 'Triplet'), ('Quadruplet', 'Quadruplet')
    ]

    tag_id = models.CharField(max_length=50, unique=True)
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    color = models.CharField(max_length=50, blank=True)
    purchase_type = models.CharField(max_length=20, choices=PURCHASE_CHOICES)
    remark = models.TextField(blank=True)

    # حقول Born At Farm
    birth_date = models.DateField(null=True, blank=True)
    birth_weight = models.FloatField(null=True, blank=True)
    mother_tag = models.CharField(max_length=50, blank=True)
    father_tag = models.CharField(max_length=50, blank=True)
    birth_type = models.CharField(max_length=20, choices=BIRTH_TYPE_CHOICES, blank=True)

    # حقول Purchased
    purchase_date = models.DateField(null=True, blank=True)
    purchase_price = models.FloatField(null=True, blank=True)
    age_months = models.IntegerField(null=True, blank=True)
    vendor_name = models.CharField(max_length=100, blank=True)

    def get_age_months(self):
        if self.birth_date:
            today = date.today()
            months = (today.year - self.birth_date.year) * 12
            months += today.month - self.birth_date.month
            return months
        return self.age_months

    def str(self):
        return self.tag_id
