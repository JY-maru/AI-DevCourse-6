from django.db import models

# Create your models here.

class Burger(models.Model):
    def __str__(self) -> str:
        return self.name #객체의 이름 출력
    
    # Feild 1
    name = models.CharField(default='', null=False, primary_key=True ,max_length=30)
    price = models.IntegerField(default=0)
    is_set = models.BooleanField(default=False)

    def save(self, *arg, **kwargs):
        if self.is_set:
            self.price += 2500
        super().save(*arg, **kwargs)