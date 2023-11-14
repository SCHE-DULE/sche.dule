from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group
from ...permissions import PERMISSIONS_MAP
from ...models import SystemUser

from django_tenants.utils import get_tenant_model, schema_context


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--schema", type=str, help="Schema name of the tenant")

    def handle(self, *args, **options):
        tenant_schema_name = options["schema"]
        
        try:
            if not tenant_schema_name:
                self.action()
            else:
                Tenant = get_tenant_model()

                tenant = Tenant.objects.get(schema_name=tenant_schema_name)
                with schema_context(tenant.schema_name):
                    self.action()

        except Exception as e:
            self.stdout.write(self.style.ERROR(e))
        except Tenant.DoesNotExist:
            self.stderr.write(
                self.style.ERROR(
                    f'Tenant with schema name "{tenant_schema_name}" does not exist'
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS("Custom permissions created successfully!")
            )

    def action(self):
        content_type = ContentType.objects.get_for_model(SystemUser)

        for user_type, permissions in PERMISSIONS_MAP.items():
            group, _ = Group.objects.get_or_create(name=user_type)

            for codename, name in permissions:
                permission, p_created = Permission.objects.get_or_create(
                    codename=codename, content_type=content_type, name=name
                )

                if not p_created:
                    permission.save()

                group.permissions.add(permission)

            group.save()
