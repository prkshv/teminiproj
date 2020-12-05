from django.db import models

# Create your models here.
class Menu(models.Model):
    menuId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name