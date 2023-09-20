from django.contrib import admin, messages
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist
from .models import Client, SystemUser, Therapist, Speciality


@admin.register(SystemUser)
class SystemUserAdmin(admin.ModelAdmin):
    list_display = ["name", "user_type"]
    search_fields = ["name", "user_type"]
    exclude = (
        'password',
        'last_login',
        'date_joined',
        'is_superuser',
        'username',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
#        'groups',
#        'user_permissions'
    )

    def save_model(self, request, obj, form, change):
        if not change:
            if not User.objects.filter(email=f"{obj.email}").exists():
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

    def change_view(self, request, object_id, form_url='', extra_context=None):
        # Fetch the SystemUser instance
        system_user = self.get_object(request, object_id)
        
        # Print information about the user
        print(f"Viewing SystemUser: {system_user.name}, Groups: {system_user.groups.all()}")

        
        # You can add any additional logic or custom code here
        
        return super().change_view(request, object_id, form_url, extra_context)



@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    search_fields = ["name"]

    class Meta:
        verbose_name = "Cliente"


@admin.register(Therapist)
class TherapistAdmin(admin.ModelAdmin):
    list_display = ["name", "crm"]
    search_fields = ["name", "crm", "specialities"]
    exclude = []


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]