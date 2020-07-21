from django.db import models

# Create your models here.
class calc_data(models.Model):
    num1=models.IntegerField()
    num2=models.IntegerField()
    result=models.IntegerField()

    def __int__(self):
        return self.result
