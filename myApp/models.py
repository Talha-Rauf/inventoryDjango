from django.db import models


# Create your models here.
class Inventory(models.Model):
    inv_name = models.CharField(max_length=264, unique=False)

    def __str__(self):
        return self.inv_name


class UserPage(models.Model):
    user = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    username = models.CharField(max_length=264, unique=False)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(UserPage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
