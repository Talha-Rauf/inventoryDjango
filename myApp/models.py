from django.db import models


# Create your models here.
class Inventory(models.Model):
    inv_name = models.CharField(max_length=264, unique=False)

    def __str__(self):
        return self.inv_name


class Users(models.Model):
    userKey = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=False)
    email = models.EmailField(max_length=264, unique=True)
    age = models.IntegerField(unique=False)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
