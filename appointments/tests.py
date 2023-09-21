import datetime
from datetime import date
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from accounts.models import Client, Speciality, SystemUser, Therapist
from .models import Appointment

class PermissionTestCase(TestCase):
    def setUp(self):

        content_type = ContentType.objects.get_for_model(SystemUser)
        permission, created = Permission.objects.get_or_create(content_type=content_type, codename="can_edit_appointment")

        # Create a user without the required permission
        self.user_without_permission = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        # Create a user with the required permission
        self.user_with_permission = User.objects.create_user(
            username="userwithpermission",
            password="testpassword"
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

        start_datetime = datetime.datetime(2023, 9, 21, 14, 0)
        end_datetime = datetime.datetime(2023, 9, 21, 15, 0)


        # Create an Appointment object
        self.appointment = Appointment.objects.create(
            client=client,
            therapist=therapist,
            service=speciality,
            appointment_date_start=start_datetime,
            appointment_date_end=end_datetime,
            status="PENDING",  # or any other valid status
            notes="",  # Add any notes as needed
        )

    def test_permission_required(self):
        # URL for the appointment update view
        url = reverse("appointment-update", args=[self.appointment.pk])

        # Test with a user without the required permission
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)  # 403 Forbidden indicates permission denied

        # Test with a user with the required permission
        self.client.login(username="userwithpermission", password="testpassword")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # 200 OK indicates successful access
