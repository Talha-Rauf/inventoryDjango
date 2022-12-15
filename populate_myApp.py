import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

import django

django.setup()

# Fake POP Script
import random
from myApp.models import AccessRecord, User
from faker import Faker
fakegen = Faker()


def populate(n=5):
    for entry in range(n):
        # get the user's name or the first entry
        fake_name = fakegen.name().split()
        first = fake_name[0]
        second = fake_name[1]

        # create the fake data for that entry
        fake_company = fakegen.company()
        fake_email = fakegen.email()
        fake_date = fakegen.date()

        # create the new inventory entry
        user = User.objects.get_or_create(first_name=first,
                                          second_name=second,
                                          company=fake_company,
                                          email=fake_email)[0]

        # create fake access record for that user
        acc_rec = AccessRecord.objects.get_or_create(name=user, date=fake_date)[0]


if __name__ == '__main__':
    print("populating script!")
    populate(10)
    print("populating complete!")
