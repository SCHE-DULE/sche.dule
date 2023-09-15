from django.test import TestCase
from .models import BaseUser, SystemUser

class SystemUserCreationTestCase(TestCase):

    def test_create_system_user(self):
        # Create a BaseUser object
        base_user = BaseUser.objects.create(
            name="John Doe",
            #email="johndoe@example.com",
            birthday="1990-01-01",
            phone_number="1234567890",
            gender="M",
        )
        

        # Create a SystemUser object associated with the BaseUser
        system_user = SystemUser.objects.create(
            baseuser_ptr=base_user,
            user_type="RECEPCIONISTA",
        )
        

        print("Base", base_user)
        print("System", system_user)

        # Query the created SystemUser object
        queried_system_user = SystemUser.objects.get(pk=system_user.pk)

        # Assert that the queried SystemUser and BaseUser objects exist
        self.assertIsNotNone(queried_system_user)
        self.assertIsNotNone(queried_system_user.baseuser_ptr)

        # Assert that the attributes of the queried SystemUser are correct
        self.assertEqual(queried_system_user.user_type, "RECEPCIONISTA")

        # Assert that the attributes of the associated BaseUser are correct
        self.assertEqual(queried_system_user.baseuser_ptr.name, "John Doe")
        self.assertEqual(queried_system_user.baseuser_ptr.email, "johndoe@example.com")
        self.assertEqual(str(queried_system_user.baseuser_ptr.birthday), "1990-01-01")
        self.assertEqual(queried_system_user.baseuser_ptr.phone_number, "1234567890")
        self.assertEqual(queried_system_user.baseuser_ptr.gender, "M")
