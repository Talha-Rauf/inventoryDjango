from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=128)
    second_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=264, unique=True)
    company = models.CharField(max_length=264)

    def __str__(self):
        return self.first_name


class AccessRecord(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
