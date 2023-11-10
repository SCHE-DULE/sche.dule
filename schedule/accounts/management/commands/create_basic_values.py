from datetime import datetime, timedelta, time
from pprint import pprint
import random
from django.core.management.base import BaseCommand

from django_tenants.utils import get_tenant_model, schema_context

from schedule.treatments.models import Speciality
from ...models import DayOfWeek, TimeSlot


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

        except Tenant.DoesNotExist:
            self.stderr.write(
                self.style.ERROR(
                    f'Tenant with schema name "{tenant_schema_name}" does not exist'
                )
            )
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING(f"Operation Cancelled"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(str(e)))
        else:
            self.stdout.write(self.style.SUCCESS(f"DB populated successfully."))

    def action(self):
        days_of_week_db_state = DayOfWeek.objects.all()

        if days_of_week_db_state.exists():
            raise Exception("DB is already populated with DayOfWeek and TimeSlot!")

        self.stdout.write(
            self.style.WARNING(f"Populate de DB with DayOfWeek and TimeSlot?")
        )
        y_or_N = input(f"Confirm? [y/N]:")

        if y_or_N == "N":
            raise Exception("Operation Cancelled")

        days_of_week_data = []

        for day, label in DayOfWeek.DAY_CHOICES:
            days_of_week_data.append(DayOfWeek(day=day))

        days_of_week_saved_data = DayOfWeek.objects.bulk_create(days_of_week_data)
        pprint(days_of_week_saved_data)
        self.stdout.write(self.style.SUCCESS("DayOfWeek Populated!!"))

        time_slots_data = []

        start_time = time(8, 0)
        end_time = time(18, 0)
        time_interval = timedelta(minutes=30)

        current_time = datetime.combine(datetime.today(), start_time)

        while current_time.time() <= end_time:
            time_slot = TimeSlot(
                start_time=current_time.time(),
                end_time=(current_time + time_interval).time(),
            )
            time_slots_data.append(time_slot)
            current_time += time_interval

        time_slot_saved_data = TimeSlot.objects.bulk_create(time_slots_data)
        pprint(time_slot_saved_data)
        self.stdout.write(self.style.SUCCESS("TimeSlot Populated!!"))
