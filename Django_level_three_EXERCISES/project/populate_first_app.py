import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()

from faker import Faker
from app.models import User
import random



fakegen = Faker()


def populate(N=5):
    for entry in range(N):

        fake_name = fakegen.name()
        fakeList = fake_name.split(" ")

        fake_firstName = fakeList[0]
        fake_lastName = fakeList[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(firstName=fake_firstName, lastName=fake_lastName, email=fake_email)[0]

if __name__ == "__main__":
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')