from django.contrib import admin
from .models import Appointment, AppointmentPackage, Room


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = [
        "client",
        "therapist",
        "service",
        "appointment_date",
        "status",
    ]
    list_filter = ["status", "service"]
    search_fields = ["client__name", "therapist__name"]
    date_hierarchy = "appointment_date"
    ordering = ["-appointment_date"]


@admin.register(AppointmentPackage)
class AppointmentPackageAdmin(admin.ModelAdmin):
    list_display = ["name", "therapist", "discounted_price"]
    search_fields = ["name", "therapist__name"]
    filter_horizontal = ["appointments"]


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ["name", "appointment_count"]
    search_fields = ["name"]
    ordering = ["name"]

    def appointment_count(self, obj):
        return obj.room_appointments.count()

    appointment_count.short_description = "Numero of Agendamentos"
