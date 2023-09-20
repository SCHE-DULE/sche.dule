from django.contrib import admin
from .models import Appointment, AppointmentPackage


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = [
        "client",
        "therapist",
        "service",
        "appointment_date_start",
        "status",
    ]
    list_filter = ["status", "service"]
    search_fields = ["client__name", "therapist__name"]
    date_hierarchy = "appointment_date_start"
    ordering = ["-appointment_date_start"]


@admin.register(AppointmentPackage)
class AppointmentPackageAdmin(admin.ModelAdmin):
    list_display = ["name", "therapist", "discounted_price"]
    search_fields = ["name", "therapist__name"]
    filter_horizontal = ["appointments"]
