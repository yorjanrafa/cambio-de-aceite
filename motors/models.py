from django.db import models

# Create your models here.
class Motors(models.Model):
    mark = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    plate = models.CharField(max_length=255)
    driver = models.CharField(max_length=255)

    def __str__(self):
        return str(f'{self.model} {self.plate}') 
