from django.contrib import admin

from .models import Benefit, Speciality, TreatmentType

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name"]

@admin.register(TreatmentType)
class TreatmentTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "color"]
    search_fields = ["name"]

@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ["title", "speciality"]
    search_fields = ["title", "speciality__name"]
