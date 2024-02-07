from django.db import models

# Create your models here.
class testData(models.Model):
    name=models.CharField(max_length=100)
    rol=models.CharField(max_length=20)

    def  __str__(self) -> str:
        return self.name