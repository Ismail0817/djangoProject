from django.db import models

# Create your models here.

class Tour(models.Model):
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return (f"ID:{self.id} "
                f"From {self.origin_country} to "
                f"{self.destination_country} for "
                f"{self.number_of_nights} nights at "
                f"{self.price} USD")
    
