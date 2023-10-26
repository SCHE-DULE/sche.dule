from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group
from ...permissions import PERMISSIONS_MAP
from ...models import SystemUser


class Command(BaseCommand):

    def handle(self, *args, **options):

        content_type = ContentType.objects.get_for_model(SystemUser)

        for user_type, permissions in PERMISSIONS_MAP.items():
            group, _ = Group.objects.get_or_create(name=user_type)

            for codename, name in permissions:

                permission, p_created = Permission.objects.get_or_create(
                    codename=codename,
                    content_type=content_type,
                    name=name
                )
                
                if not p_created:
                    permission.save()                
                
                group.permissions.add(permission)
            
            group.save() 


        self.stdout.write(self.style.SUCCESS('Custom permissions created successfully!'))
