from django.db import models

class Vaccine(models.Model):
    name = models.CharField(max_length=100)
    given_every_days = models.IntegerField()

    def str(self):
        return self.name
