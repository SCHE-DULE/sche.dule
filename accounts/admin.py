from django.contrib import admin, messages
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist
from .models import Client, SystemUser, Therapist, Speciality


@admin.register(SystemUser)
class SystemUserAdmin(admin.ModelAdmin):
    list_display = ["name", "user"]
    search_fields = ["name", "user"]
    exclude = ["user"]

    def save_model(self, request, obj, form, change):
        if not change:
            if not User.objects.filter(email=f"{obj.email}").exists():
                try:
                    print(request)
                    request.user.baseuser
                except ObjectDoesNotExist:
                    super().save_model(request, obj, form, change)
                else:
                    messages.set_level(request, messages.ERROR)
                    messages.error(
                        request, "Você não pode cadastrar mais de um usuário!"
                    )
            else:
                messages.error(request, "Este email já está sendo usado!")
        obj.save()


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "user"]
    search_fields = ["name"]
    exclude = ["user"]


@admin.register(Therapist)
class TherapistAdmin(admin.ModelAdmin):
    list_display = ["name", "crm", "avaliability_days", "hours", "rate"]
    search_fields = ["name", "crm"]
    exclude = ["user"]


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]