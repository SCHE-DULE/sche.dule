from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist
from .models import (
    BaseUser,
    Client,
    SystemUser,
    Therapist,
    TimeSlot,
    DayOfWeek,
)


@admin.register(SystemUser)
class SystemUserAdmin(UserAdmin):
    list_display = ["name", "user_type"]
    search_fields = ["name", "user_type"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "password1",
                    "password2",
                ),
            },
        ),
        (
            "Personal Info",
            {"fields": ("name", "email", "birthday", "phone_number", "gender", "photo")},
        ),
        ("Type of User", {"fields": ("user_type",)}),
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal Info",
            {"fields": ("name", "email", "birthday", "phone_number", "gender", "photo")},
        ),
        ("Permissions", {"fields": ("is_active",)}),
        ("Type of User", {"fields": ("user_type",)}),
    )

    # Exclude the following fields
    exclude = ("groups", "user_permissions")

    def save_model(self, request, obj, form, change):
        if not change:
            if not BaseUser.objects.filter(email=f"{obj.email}").exists():
                try:
                    request.user.id
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

    def change_view(self, request, object_id, form_url="", extra_context=None):
        # Fetch the SystemUser instance
        system_user = self.get_object(request, object_id)

        # Print information about the user
        print(
            f"Viewing SystemUser: {system_user.name}, Groups: {system_user.groups.all()}"
        )

        # You can add any additional logic or custom code here

        return super().change_view(request, object_id, form_url, extra_context)


@admin.register(Client)
class ClientAdmin(UserAdmin):
    list_display = ["name", "email"]
    search_fields = ["name"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "password1",
                    "password2",
                ),
            },
        ),
        (
            "Personal Info",
            {"fields": ("name", "email", "birthday", "phone_number", "gender")},
        ),
        (
            "Client Info",
            {
                "fields": (
                    "cpf",
                    "rg_or_rne",
                    "photo",
                )
            },
        ),
        (
            "Client Address",
            {
                "fields": (
                    "street_address",
                    "number",
                    "zip_code",
                    "neighborhood",
                    "city",
                    "state",
                    "country",
                )
            },
        ),
        (
            None,
            {"fields": ("observation",)},
        ),
    )

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal Info",
            {"fields": ("name", "email", "birthday", "phone_number", "gender")},
        ),
        (
            "Permissions",
            {"fields": ("is_active",)},
        ),
        (
            "Client Info",
            {
                "fields": (
                    "cpf",
                    "rg_or_rne",
                    "photo",
                )
            },
        ),
        (
            "Client Address",
            {
                "fields": (
                    "street_address",
                    "number",
                    "zip_code",
                    "neighborhood",
                    "city",
                    "state",
                    "country",
                )
            },
        ),
        (
            None,
            {"fields": ("observation",)},
        ),
    )

    # Exclude the following fields
    exclude = ("groups", "user_permissions")

    class Meta:
        verbose_name = "Cliente"


@admin.register(Therapist)
class TherapistAdmin(UserAdmin):
    list_display = ["name", "council"]
    search_fields = ["name", "council", "specialities"]

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "password1",
                    "password2",
                ),
            },
        ),
        (
            "Personal Info",
            {
                "fields": ("name", "email", "birthday", "phone_number", "gender"),
            },
        ),
        (
            "Therapist Info",
            {
                "fields": (
                    "specialities",
                    "council",
                    "rate",
                    "fee",
                    "photo",
                    "contract_scan",
                ),
            },
        ),
        (
            "Availability",
            {
                "fields": ("availability_hours", "availability_days"),
            },
        ),
    )

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal Info",
            {
                "fields": ("name", "email", "birthday", "phone_number", "gender"),
            },
        ),
        (
            "Permissions",
            {
                "fields": ("is_active",),
            },
        ),
        (
            "Therapist Info",
            {
                "fields": (
                    "specialities",
                    "council",
                    "rate",
                    "fee",
                    "photo",
                    "contract_scan",
                ),
            },
        ),
        (
            "Availability",
            {
                "fields": ("availability_hours", "availability_days"),
            },
        ),
    )

    # Exclude the following fields
    exclude = ("groups", "user_permissions")


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ["start_time", "end_time"]


@admin.register(DayOfWeek)
class DayOfWeekAdmin(admin.ModelAdmin):
    list_display = ["day"]
