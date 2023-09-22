from django.test import TestCase

from ..models import Client, SystemUser


class ClientUserTestCase(TestCase):
    def setUp(self) -> None:
        self.client_data = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "birthday": "1990-01-01",
            "phone_number": "1234567890",
            "gender": "M",
            "cpf": "12345678901",
            "rg_or_rne": "134434",
            "country": "Bosnia",
            "state": "Province",
            "city": "capital",
            "neighborhood": "none",
            "zip_code": "34234343",
            "street_address": "Rua zero",
            "number": "123",
        }

        return super().setUp()

    def test_create_client(self):
        client_data = self.client_data  # Get client data
        client_user = Client.objects.create(
            name=client_data["name"],
            email=client_data["email"],
            birthday=client_data["birthday"],
            phone_number=client_data["phone_number"],
            gender=client_data["gender"],
            cpf=client_data["cpf"],
            rg_or_rne=client_data["rg_or_rne"],
            country=client_data["country"],
            state=client_data["state"],
            city=client_data["city"],
            neighborhood=client_data["neighborhood"],
            zip_code=client_data["zip_code"],
            street_address=client_data["street_address"],
            number=client_data["number"],
        )

        print("client_user", client_user)

        queried_client = Client.objects.get(pk=client_user.pk)

        self.assertIsNotNone(queried_client)
        self.assertIsNotNone(queried_client.baseuser_ptr)

        self.assertEqual(queried_client.cpf, client_data["cpf"])
        self.assertEqual(queried_client.rg_or_rne, client_data["rg_or_rne"])
        self.assertEqual(queried_client.country, client_data["country"])
        self.assertEqual(queried_client.state, client_data["state"])
        self.assertEqual(queried_client.city, client_data["city"])
        self.assertEqual(queried_client.neighborhood, client_data["neighborhood"])
        self.assertEqual(queried_client.zip_code, client_data["zip_code"])
        self.assertEqual(queried_client.street_address, client_data["street_address"])
        self.assertEqual(queried_client.number, client_data["number"])

        self.assertEqual(queried_client.baseuser_ptr.name, "John Doe")
        self.assertEqual(queried_client.baseuser_ptr.email, "johndoe@example.com")
        self.assertEqual(str(queried_client.baseuser_ptr.birthday), "1990-01-01")
        self.assertEqual(queried_client.baseuser_ptr.phone_number, "1234567890")
        self.assertEqual(queried_client.baseuser_ptr.gender, "M")