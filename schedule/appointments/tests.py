import datetime
from datetime import date
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from accounts.models import Client, SystemUser, Therapist, TimeSlot
from treatments.models import Speciality
from .models import Appointment


class PermissionTestCase(TestCase):
    def setUp(self):
        content_type = ContentType.objects.get_for_model(SystemUser)

        permission, created = Permission.objects.get_or_create(
            content_type=content_type,
            codename="can_edit_appointment",
        )

        # Create a user without the required permission
        self.user_without_permission = SystemUser.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            birthday="1990-01-01",
            phone_number="1234567890",
            gender="M",
            username="testuser",
            password="testpassword",
            user_type="RECEPTIONIST",
        )

        # Create a user with the required permission
        self.user_with_permission = SystemUser.objects.create(
            name="User With Permission",
            email="userwithpermission@example.com",
            birthday="1990-01-01",
            phone_number="1234567890",
            gender="M",
            username="userwithpermission",
            password="testpassword",
            user_type="MANAGER",
        )
        self.user_with_permission.user_permissions.add(permission)

        client = Client.objects.create(
            name="pessoinha pereira",
            email="pemd@fmd.com",
            birthday=date(2023, 9, 21),
            phone_number="134141347798675",
            gender="F",
            baseuser_ptr_id=1,
            cpf="3498597",
            rg_or_rne="593504",
            country="Brazil",
            state="AC",
            city="Rio Branco",
            neighborhood="Tucuma",
            zip_code="69919-775",
            street_address="Rua W1",
            number="252",
            complement_address=None,
            observation="",
        )

        # Create a Therapist object
        therapist = Therapist.objects.create(
            name="Juninho Maroto",
            email="mao@fmi.com",
            birthday=date(2023, 9, 21),
            phone_number="3095434",
            gender="M",
            baseuser_ptr_id=2,
            crm="352543254",
            rate=300.00,
            fee=50.00,
            photo="terapeutas/16948847957744.jpg",
            contract_scan="contratos/169474719810337_dhqrm0W.png",
        )

        # Create a Speciality object
        speciality = Speciality.objects.create(name="Massage")

        start_datetime = datetime.date(2023, 9, 21)
        time_slot = TimeSlot.objects.create(
            start_time=datetime.time(9, 0), end_time=datetime.time(10, 0)
        )

        # Create an Appointment object
        self.appointment = Appointment.objects.create(
            client=client,
            therapist=therapist,
            service=speciality,
            appointment_date=start_datetime,
            appointment_time_slot=time_slot,
            status="PENDING",  # or any other valid status
            notes="",  # Add any notes as needed
        )

    def test_permission_required(self):
        # URL for the appointment update view
        url = reverse("appointment-update", args=[self.appointment.pk])

        # Test with a user without the required permission
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, "/accounts/login/?next=/appointments/1/update/"
        )  # 302 tests redirection

        # Test with a user with the required permission
        self.client.login(username="userwithpermission", password="testpassword")
        response = self.client.get(url, follow=True)
        self.assertEqual(
            response.status_code, 200
        )  # 200 OK indicates successful access
