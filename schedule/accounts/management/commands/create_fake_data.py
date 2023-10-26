from django.db.models import Q
from datetime import date, datetime, timedelta, time
from pprint import pprint
import random
from django.core.management.base import BaseCommand

from appointments.models import Appointment, Room
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

service_names = [
    "Taxa de Deslocamento",
    "Psicologia - Consulta",
    "Psicologia - Sessão",
    "Avaliação BIA",
    "Consulta Biomedica",
    "Consulta Dermatológica",
    "Consulta Floral",
    "Consulta Médica",
    "Consulta ou Atendimento Domiciliar",
    "Consultas, Emergência e Consultas Nutrição",
    "Escaneamento Corporal",
    "Ozonoterapia - Avaliação",
    "Ryodoraku",
    "Tratamento Dermatológico",
    "Drenagem Linfática Facial",
    "Drenagem Linfática Manual Corporal",
    "Massagem com Pedras Quentes",
    "Massagem Modeladora",
    "Massagem Relaxante",
    "Massagens",
    "Barras de Access",
    "Acupuntura",
    "Bioressonancia",
    "BodyTalk",
    "Consultas on-line",
    "Microfisioterapia",
    "Osteopatia",
    "Ozonio - Isolada",
    "Ozônio - Upgrade",
    "Ozônioterapia",
    "Quiropraxia",
    "Reiki",
    "Terapia Integrativa",
    "Terapia Manual",
    "Yoga Restaurativa",
    "Hidrobiorecuperação",
    "Consulta Clinica",
    "Procedimentos cirurgicos",
    "Fisioterapia",
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        locales = ["en_US", "pt_BR", "fr_FR", "es_ES"]

        fake = Faker()

        try:
            self.stdout.write(
                self.style.WARNING(f"Populate de DB with fake random data and quantities automatically?")
            )
            y_or_N = input(f"Confirm? [y/N]:")
            if y_or_N.strip().upper() == "N" or y_or_N.strip().upper() == "":
                qtd = int(input(f"How many System Users do you want to create: "))
                if qtd > 0:
                    self.create_system_users(fake, qtd)

                qtd = int(input(f"How many Clients do you want to create: "))
                if qtd > 0:
                    self.create_clients(fake, qtd)

                qtd = int(input(f"How many Treatment Types do you want to create: "))
                if qtd > 0:
                    self.create_treatment_types(fake, qtd)

                qtd = int(input(f"How many Specialities do you want to create: "))
                if qtd > 0:
                    self.create_specialities(fake, qtd)

                qtd = int(input(f"How many Therapists do you want to create: "))
                if qtd > 0:
                    self.create_therapists(fake, qtd)

                qtd = int(input(f"How many Appointments do you want to create: "))
                if qtd > 0:
                    self.create_appointments(fake, qtd)
            elif y_or_N.strip().upper() == "Y":
                self.create_system_users(fake, random.randint(1, 10))

                self.create_clients(fake, random.randint(10, 20))

                self.create_treatment_types(fake, random.randint(3, 8))

                self.create_specialities(fake, random.randint(10, 15))

                self.create_therapists(fake, random.randint(10, 20))

                self.create_appointments(fake, random.randint(10, 20))
            else:
                raise Exception("Operation Cancelled")
        
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING(f"Operation Cancelled"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(str(e)))
        else:
            self.stdout.write(self.style.SUCCESS("Fake data created successfully!!"))

    def create_system_users(self, fake, num_users):
        self.stdout.write(self.style.WARNING(f"Creating data for SystemUsers"))

        user_data = []

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
                photo=f"placeholder/terapeutas/{fake.random_element([1,5,6,7])}.png",
            )
            system_user.save()
            user_data.append(system_user)

        print(f"System Users created: {len(user_data)}")

    def create_clients(self, fake, num_clients):
        self.stdout.write(self.style.WARNING(f"Creating data for Clients"))
        client_data = []

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
                photo=f"placeholder/terapeutas/{fake.random_element([1,5,6,7])}.png",
            )
            client.save()
            client_data.append(client)

        print(f"Clients created: {len(client_data)}")

    def create_treatment_types(self, fake, num_treatment_type):
        self.stdout.write(self.style.WARNING(f"Creating data for Treatment Types"))
        treatment_type_data = []

        for _ in range(num_treatment_type):
            name = fake.unique.word()
            color = random.choice(COLOR_CHOICES)[
                0
            ]  # Choose a random color from COLOR_CHOICES

            fake_treatment_type = TreatmentType(name=name, color=color)
            fake_treatment_type.save()
            treatment_type_data.append(fake_treatment_type)

        print(f"Treatment Types created: {len(treatment_type_data)}")

    def create_specialities(self, fake, num_specialities):
        self.stdout.write(self.style.WARNING(f"Creating data for Specialities"))
        specialities_data = []

        treatment_types = TreatmentType.objects.all().order_by("?")

        for _ in range(num_specialities):
            name = fake.unique.word()
            treatment_type = random.choice(treatment_types)

            fake_speciality = Speciality(
                name=random.choice(service_names),
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

    def create_therapists(self, fake, num_therapists):
        self.stdout.write(self.style.WARNING(f"Creating data for Therapists"))
        therapist_data = []

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

    def create_appointments(self, fake, num_appointments):
        self.stdout.write(self.style.WARNING(f"Creating data for Appointments"))
        appointments = []

        for _ in range(0, num_appointments):
            while True:
                appointment = self.create_appointment(fake)

                overlapping_appointments = Appointment.objects.filter(
                    Q(appointment_date=appointment.appointment_date)
                    & ~Q(id=appointment.pk)
                    & Q(
                        Q(
                            time_start__lte=appointment.time_start,
                            time_end__gt=appointment.time_start,
                        )
                        | Q(
                            time_start__lt=appointment.time_end,
                            time_end__gte=appointment.time_end,
                        )
                        | Q(
                            time_start__gte=appointment.time_start,
                            time_end__lte=appointment.time_end,
                        )
                    )
                    & Q(room=appointment.room)
                )
                if overlapping_appointments.exists() is False:
                    appointment.save()
                    appointments.append(appointment)
                    break

    def create_appointment(self, fake) -> Appointment:
        random_index = random.randint(0, Client.objects.count() - 1)
        random_client = Client.objects.all().order_by("?")[random_index]

        random_index = random.randint(0, Speciality.objects.count() - 1)
        random_service = Speciality.objects.all().order_by("?")[random_index]

        while True:
            random_therapist = (
                Therapist.objects.filter(specialities=random_service)
                .all()
                .order_by("?")
                .first()
            )
            if random_therapist is not None:
                break
            else:
                random_index = random.randint(0, Speciality.objects.count() - 1)
                random_service = Speciality.objects.all().order_by("?")[random_index]

        random_index = random.randint(0, Room.objects.count() - 1)
        random_room = Room.objects.all().order_by("?")[random_index]

        current_date = date.today()
        one_year_from_now = current_date + timedelta(days=2)
        appointment_date = fake.date_between_dates(
            date_start=current_date, date_end=one_year_from_now
        )

        start_time = time(fake.random_int(min=8, max=16), (fake.random_int(min=0, max=1) * 30))  # type: ignore

        time_difference = timedelta(minutes=random.randint(0, 3) * 30)
        end_time = (
            datetime.combine(appointment_date, start_time) + time_difference
        ).time()

        appointment = Appointment(
            client=random_client,
            therapist=random_therapist,
            service=random_service,
            appointment_date=appointment_date,
            time_start=start_time,
            time_end=end_time,
            room=random_room,
            status=fake.random_element(
                elements=[choice[0] for choice in Appointment.STATUS_CHOICES]
            ),
            notes=fake.text(max_nb_chars=200),
        )

        return appointment
