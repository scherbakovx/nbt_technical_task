import random

from django.core.management.base import BaseCommand

from faker import Faker

from api.models import Company, Device, Measurement


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        Company.objects.all().delete()
        Device.objects.all().delete()
        Measurement.objects.all().delete()

        fake = Faker()

        for _ in range(10):
            name = fake.company()
            location = fake.address()

            Company.objects.create(name=name, location=location)

        for _ in range(30):
            company = Company.objects.order_by('?').first()
            active = random.choice([False, True])
            device_id = fake.bothify(text='???-########-####-######')
            labels = fake.words(nb=3)

            Device.objects.create(company=company, active=active, device_id=device_id, labels=labels)


        for i in range(150):
            device = Device.objects.order_by('?').first()
            date = fake.date_time(tzinfo=fake.pytimezone())
            data = {
                "temperature": fake.pyfloat(right_digits=2, min_value=20.0, max_value=38.0),
                "rssi": fake.pyint(min_value=0, max_value=45),
                "humidity": fake.pyfloat(right_digits=2, min_value=20.0, max_value=100.0),
            }

            Measurement.objects.create(device=device, date=date, data=data)
