from datetime import date, datetime, timedelta, time
from pprint import pprint
import random
from django.core.management.base import BaseCommand

from appointments.models import Appointment
from treatments.models import COLOR_CHOICES, Benefit, Speciality, TreatmentType
from ...models import (
    BaseUser,
    Client,
    DayOfWeek,
    SystemUser,
    Therapist,
    TimeSlot,
)
from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **options):
        locales = ["en_US", "pt_BR", "fr_FR", "es_ES"]

        fake = Faker()

        self.stdout.write(self.style.WARNING(f"Creating data for SystemUsers"))

        user_data = []
        num_users = random.randint(10, 20)

        for _ in range(0, num_users):
            profile = fake.profile()
            system_user = SystemUser(
                username=profile["username"],
                name=profile["name"],
                email=profile["mail"],
                birthday=profile["birthdate"],
                phone_number=fake.phone_number(),
                gender=fake.random_element(
                    elements=[choice[0] for choice in BaseUser.GENDER_CHOICES]
                ),
                user_type=fake.random_element(
                    elements=[choice[0] for choice in SystemUser.USER_TYPE]
                ),
            )
            system_user.save()
            user_data.append(system_user)

        print(f"System Users created: {len(user_data)}")
        self.stdout.write(self.style.WARNING(f"Creating data for Clients"))

        client_data = []
        num_clients = random.randint(10, 30)

        for _ in range(num_clients):
            profile = fake.profile()

            client = Client(
                username=profile["username"],
                name=profile["name"],
                email=profile["mail"],
                birthday=profile["birthdate"],
                phone_number=fake.phone_number(),
                gender=fake.random_element(
                    elements=[choice[0] for choice in BaseUser.GENDER_CHOICES]
                ),
                cpf=fake.unique.random_int(min=10000000000, max=99999999999),
                rg_or_rne=profile["ssn"],
                country=fake.country(),
                state=fake.state(),
                city=fake.city(),
                neighborhood=fake.street_name(),
                zip_code=fake.zipcode(),
                street_address=fake.street_address(),
                number=fake.building_number(),
                complement_address=fake.secondary_address(),
                observation=fake.paragraph(),
            )
            client.save()
            client_data.append(client)

        print(f"Clients created: {len(client_data)}")
        self.stdout.write(self.style.WARNING(f"Creating data for Treatment Types"))

        treatment_type_data = []
        num_treatment_type = random.randint(3, 8)

        for _ in range(num_treatment_type):
            name = fake.unique.word()
            color = random.choice(COLOR_CHOICES)[0]  # Choose a random color from COLOR_CHOICES
            
            fake_treatment_type = TreatmentType(name=name, color=color)
            fake_treatment_type.save()
            treatment_type_data.append(fake_treatment_type)

        print(f"Treatment Types created: {len(treatment_type_data)}")
        self.stdout.write(self.style.WARNING(f"Creating data for Specialities"))

        specialities_data = []
        num_specialities = random.randint(10, 15)

        treatment_types = TreatmentType.objects.all()

        for _ in range(num_specialities):
            name = fake.unique.word()  
            treatment_type = random.choice(treatment_types)
            
            fake_speciality = Speciality(
                name=name,
                description=fake.paragraph(),
                feature_img=f"placeholder/terapias/{fake.random_element([1, 2, 3, 4])}.jpg",
                treatment_type=treatment_type,
            )
            fake_speciality.save()

            num_fake_benefits = random.randint(2, 5)
            for _ in range(num_fake_benefits):
                benefit = Benefit(
                    speciality=fake_speciality,
                    title=fake.unique.word(),
                    description=fake.paragraph(),
                )
                benefit.save()

            specialities_data.append(fake_speciality)

        print(f"Specialities created: {len(specialities_data)}")
        self.stdout.write(self.style.WARNING(f"Creating data for Therapists"))

        therapist_data = []
        num_therapists = random.randint(10, 20)

        for _ in range(num_therapists):
            profile = fake.profile()
            therapist = Therapist(
                username=profile["username"],
                name=profile["name"],
                email=profile["mail"],
                birthday=profile["birthdate"],
                phone_number=fake.phone_number(),
                gender=fake.random_element(
                    elements=[choice[0] for choice in BaseUser.GENDER_CHOICES]
                ),
                crm=fake.random_int(min=100000, max=999999),
                rate=fake.pydecimal(left_digits=2, right_digits=2, positive=True),
                fee=fake.pydecimal(
                    left_digits=2,
                    right_digits=2,
                    positive=True,
                ),
                photo=f"placeholder/terapeutas/{fake.random_element([1,5,6,7])}.png",
                contract_scan="placeholder/contratos/contrato-1.jpeg",
            )

            therapist.save()

            num_specialities = fake.random_int(min=1, max=5)
            therapist.specialities.set(
                Speciality.objects.order_by("?")[:num_specialities]
            )

            num_time_slots = fake.random_int(min=1, max=11)
            therapist.availability_hours.set(
                TimeSlot.objects.order_by("?")[:num_time_slots]
            )

            num_days = fake.random_int(min=1, max=5)
            therapist.availability_days.set(DayOfWeek.objects.order_by("?")[:num_days])

            therapist.save()

            therapist_data.append(therapist)

        pprint(therapist_data)

        self.stdout.write(self.style.WARNING(f"Creating data for Appointments"))

        num_appointments = random.randint(10, 20)
        appointments = []

        for _ in range(0, num_appointments):
            random_index = random.randint(0, Client.objects.count() - 1)
            random_client = Client.objects.all().order_by("?")[random_index]

            random_index = random.randint(0, Therapist.objects.count() - 1)
            random_therapist = Therapist.objects.all().order_by("?")[random_index]

            random_index = random.randint(0, Speciality.objects.count() - 1)
            random_service = Speciality.objects.all().order_by("?")[random_index]

            random_index = random.randint(0, TimeSlot.objects.count() - 1)
            random_time_slot = TimeSlot.objects.all().order_by("?")[random_index]

            current_date = date.today()
            one_year_from_now = current_date + timedelta(days=30)
            appointment_date = fake.date_between_dates(
                date_start=current_date, date_end=one_year_from_now
            )

            appointment = Appointment(
                client=random_client,
                therapist=random_therapist,
                service=random_service,
                appointment_date=appointment_date,
                appointment_time_slot=random_time_slot,
                status=fake.random_element(
                    elements=[choice[0] for choice in Appointment.STATUS_CHOICES]
                ),
                notes=fake.text(max_nb_chars=200),
            )

            appointment.save()
            appointments.append(appointment)

        self.stdout.write(self.style.SUCCESS("Fake data created successfully!!"))
