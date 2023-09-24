import getpass
from django.core.management.base import BaseCommand
from django.forms import ValidationError
from ...models import SystemUser
from django.core.validators import EmailValidator


class Command(BaseCommand):
    help = "Create a super admin user"

    def handle(self, *args, **options):
        username = input("Enter a username for the super admin: ")

        try:
            if SystemUser.objects.filter(username=username).exists():
                self.stdout.write(
                    self.style.WARNING("A user with the provided name already exists.")
                )
            else:
                tries = 0

                while tries < 3:
                    email = input("Enter a email for the super admin: ")
                    validate_email = EmailValidator()
                    validated = False

                    try:
                        validate_email(email)
                    except ValidationError:
                        validated = False
                    else:
                        validated = True

                    if validated:
                        break
                    else:
                        tries += 1
                        self.stdout.write(
                            self.style.WARNING(
                                f"Error: Enter a valid email address, you have {(tries - 3) * -1} attempts left"
                            )
                        )

                    if tries >= 3:
                        raise Exception("Operation Cancelled - Maximum tries")

                name = input("Enter the super admin's full name: ")
                tries = 0

                while tries < 3:
                    password = getpass.getpass("Enter a password for the super admin: ")
                    password2 = getpass.getpass(
                        "Enter a password for the super admin (again): "
                    )

                    if password == password2:
                        break
                    else:
                        tries += 1
                        self.stdout.write(
                            self.style.WARNING(
                                f"Error: Your passwords didn't match, you have {(tries - 3) * -1} attempts left"
                            )
                        )

                    if tries >= 3:
                        raise Exception("Operation Cancelled - Maximum tries")

                y_or_N = input(
                    f"Create a super admin user with the name {username}? [y/N]:"
                )

                if y_or_N == "N":
                    raise Exception("Operation Cancelled")

                super_admin = SystemUser.objects.create_superuser(
                    name=name,
                    username=username,
                    email=email,
                    password=password,
                    user_type="SUPER_ADMIN",
                    birthday="1990-01-01",
                    phone_number="1234567890",
                    gender="M",
                )

        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING(f"Operation Cancelled"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(e))
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f'Super admin user "{super_admin.username}" created successfully.'
                )
            )
