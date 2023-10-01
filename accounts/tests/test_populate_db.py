from datetime import date, datetime, timedelta, time
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group
from django.utils import timezone
from django.shortcuts import get_object_or_404
from pprint import pprint
import random

from django.test import TestCase

from appointments.models import Appointment

from ..permissions import PERMISSIONS_MAP
from ..models import (
    BaseUser,
    Client,
    DayOfWeek,
    SystemUser,
    Therapist,
    TimeSlot,
    Speciality,
)
from faker import Faker


class SystemUserCreationTestCase(TestCase):
    service_names = [
        "Taxa de Deslocamento",
        "Psicologia - Consulta",
        "Psicologia - Sessão",
        "Avaliação BIA",
        "Consulta",
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

    def setUp(self) -> None:
        content_type = ContentType.objects.get_for_model(SystemUser)

        for user_type, permissions in PERMISSIONS_MAP.items():
            group, g_created = Group.objects.get_or_create(name=user_type)

            for codename, name in permissions:
                permission, p_created = Permission.objects.get_or_create(
                    codename=codename, content_type=content_type, name=name
                )

                if not p_created:
                    permission.save()

                group.permissions.add(permission)

            group.save()

        return super().setUp()

    def test_create_users(self):
        fake = Faker()

        num_users = random.randint(4, 7)

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

        self.assertEqual(SystemUser.objects.count(), num_users)

    def test_create_clients(self):
        self.create_clients()

    def test_create_therapist(self):
        self.create_therapists()

    def test_create_appointments(self):
        self.create_clients()
        self.create_therapists()

        fake = Faker()

        num_appointments = random.randint(4, 7)
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
            one_year_from_now = current_date + timedelta(days=365)
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

        pprint(appointments)

        self.assertEqual(Appointment.objects.count(), len(appointments))

    def create_clients(self):
        fake = Faker()

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

        self.assertEqual(Client.objects.count(), num_clients)

    def create_therapists(self):
        fake = Faker()

        num_therapists = random.randint(10, 20)

        speciality_data = []
        for service in self.service_names:
            speciality = Speciality(name=service)
            speciality_data.append(speciality)

        speciality_saved_data = Speciality.objects.bulk_create(speciality_data)

        self.assertEqual(Speciality.objects.count(), len(speciality_data))

        time_slots_data = []

        start_time = time(8, 0)
        end_time = time(18, 0)
        time_interval = timedelta(hours=1)

        current_time = datetime.combine(datetime.today(), start_time)

        while current_time.time() <= end_time:
            time_slot = TimeSlot(
                start_time=current_time.time(),
                end_time=(current_time + time_interval).time(),
            )
            time_slots_data.append(time_slot)
            current_time += time_interval

        time_slot_saved_data = TimeSlot.objects.bulk_create(time_slots_data)

        self.assertEqual(TimeSlot.objects.count(), len(time_slots_data))

        days_of_week_data = []

        for day, label in DayOfWeek.DAY_CHOICES:
            days_of_week_data.append(DayOfWeek(day=day))

        days_of_week_saved_data = DayOfWeek.objects.bulk_create(days_of_week_data)

        self.assertEqual(DayOfWeek.objects.count(), len(days_of_week_data))

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
                photo=f"placeholder/terapeutas/{fake.random_element([1,5,6,7])}.jpg",
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

        self.assertEqual(Therapist.objects.count(), num_therapists)
