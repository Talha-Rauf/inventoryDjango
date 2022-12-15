import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

import django

django.setup()

# Fake POP Script
import random
from myApp.models import AccessRecord, User, Inventory
from faker import Faker

fakegen = Faker()
topics = ['Max', 'Bob', 'Sam', 'John']


def add_Inv():
    # t = Inventory.objects.create('User Inventory')[0]

    t = Inventory.objects.get_or_create(inv_name=random.choice(topics))[0]
    # [0] means the returning parameter is a tuple, so we grab the first object
    t.save()
    return t


def populate(n=5):
    for entry in range(n):
        # get the topic or the entry
        inv = add_Inv()

        # create the fake data for that entry
        fake_url = fakegen.url()

        fake_name = fakegen.company()
        fake_email = fakegen.email()
        fake_date = fakegen.date()

        # create the new inventory entry
        user = User.objects.get_or_create(userKey=inv, name=fake_name, url=fake_url, email=fake_email)[0]

        # create fake access record for that user
        acc_rec = AccessRecord.objects.get_or_create(name=user, date=fake_date)[0]


if __name__ == '__main__':
    print("populating script!")
    populate(10)
    print("populating complete!")
