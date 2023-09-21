from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from accounts.models import SystemUser

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        permissions = [
            ("can_create_client", "Pode cadastrar Cliente"),
            ("can_view_client_info", "Pode ver informações de Cliente"),
            ("can_view_client_list", "Pode ver lista de Cliente"),
            ("modify_patient_information", "Pode editar informações de Cliente"),
            ("can_create_therapist", "Pode cadastrar terapeuta"),
            ("can_view_therapist_info", "Pode ver informações de terapeuta"),
            ("can_view_therapist_list", "Pode ver lista de terapeuta"),
            ("modify_therapist_information", "Pode editar informações de terapeuta"),
            ("manage_system_users", "Pode gerenciar usuários do sistema"),
            # Add more permissions as needed
        ]

        content_type = ContentType.objects.get_for_model(SystemUser)

        for codename, name in permissions:
            
            permission, _ = Permission.objects.get_or_create(
                codename=codename,
                content_type=content_type,
            )
            permission.name = name
            permission.save()

        self.stdout.write(self.style.SUCCESS('Custom permissions created successfully!'))
