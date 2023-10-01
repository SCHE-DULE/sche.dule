from datetime import datetime, timedelta, time
from pprint import pprint
import random
from django.core.management.base import BaseCommand
from ...models import DayOfWeek, TimeSlot, Speciality


class Command(BaseCommand):
    def handle(self, *args, **options):

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

        try:
            self.stdout.write(self.style.WARNING(f"Populate de DB with DayOfWeek, TimeSlot, and Speciality?"))
            y_or_N = input(
                f"Confirm? [y/N]:"
            )

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
            pprint(time_slot_saved_data)
            self.stdout.write(self.style.SUCCESS("TimeSlot Populated!!"))

            speciality_data = []
            for service in service_names:
                speciality = Speciality(
                    name=service
                )
                speciality_data.append(speciality)

            speciality_saved_data = Speciality.objects.bulk_create(speciality_data)
            pprint(speciality_saved_data)
            self.stdout.write(self.style.SUCCESS("DayOfWeek Populated!!"))
        
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING(f"Operation Cancelled"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(str(e)))
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f'DB populated successfully.'
                )
            )