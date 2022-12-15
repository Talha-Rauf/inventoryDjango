from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=264, unique=False)

    def __str__(self):
        return self.user_name


class UserPage(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=264, unique=False)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(UserPage)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
