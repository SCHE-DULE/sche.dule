from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from .models import Client, Therapist, SystemUser


class ClientListView(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = "accounts.can_view_client_list"
    model = Client
    template_name = "client/client_list.html"
    context_object_name = "clients"


class ClientCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = "accounts.can_create_client"
    model = Client
    template_name = "client/client_form.html"
    fields = [
        "name",
        "email",
        "birthday",
        "phone_number",
        "gender",
        "cpf",
        "rg_or_rne",
        "country",
        "state",
        "city",
        "neighborhood",
        "zip_code",
        "street_address",
        "number",
        "complement_address",
    ]
    success_url = reverse_lazy("client_list")


class ClientUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = "accounts.can_view_client_info"
    model = Client
    template_name = "client/client_form.html"
    fields = [
        "name",
        "email",
        "birthday",
        "phone_number",
        "gender",
        "cpf",
        "rg_or_rne",
        "country",
        "state",
        "city",
        "neighborhood",
        "zip_code",
        "street_address",
        "number",
        "complement_address",
    ]
    success_url = reverse_lazy("client_list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        user = self.request.user
        print(user.get_all_permissions())
        if not user.has_perm("accounts.modify_patient_information"):
            excluded_fields = [
                "cpf",
                "rg_or_rne",
                "country",
                "state",
                "city",
                "neighborhood",
                "zip_code",
                "street_address",
                "number",
                "complement_address",
            ]
            for field_name in excluded_fields:
                if field_name in form.fields:
                    form.fields.pop(field_name)

        return form


class ClientDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = "accounts.modify_patient_information"
    model = Client
    template_name = "client/client_confirm_delete.html"
    success_url = reverse_lazy("client_list")


class ClientDetailView(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = "accounts.can_view_client_info"
    model = Client
    template_name = "client/client_detail.html"
    context_object_name = "client"


class SystemUserListView(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = "accounts.manage_system_users"
    model = SystemUser
    template_name = "systemuser/systemuser_list.html"
    context_object_name = "systemusers"


class SystemUserCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = "accounts.manage_system_users"
    model = SystemUser
    fields = [
        "name",
        "email",
        "birthday",
        "phone_number",
        "gender",
        "user_type",
    ]
    template_name = "systemuser/systemuser_form.html"
    success_url = reverse_lazy("systemuser_list")


class SystemUserUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = "accounts.manage_system_users"
    model = SystemUser
    fields = [
        "name",
        "email",
        "birthday",
        "phone_number",
        "gender",
        "user_type",
    ]
    template_name = "systemuser/systemuser_form.html"
    success_url = reverse_lazy("systemuser_list")


class SystemUserDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = "accounts.manage_system_users"
    model = SystemUser
    template_name = "systemuser/systemuser_delete.html"
    success_url = reverse_lazy("systemuser_list")


class SystemUserDetailView(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = "accounts.manage_system_users"
    model = SystemUser
    template_name = "systemuser/systemuser_detail.html"
    context_object_name = "systemuser"


class TherapistListView(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = "accounts.can_view_therapist_list"
    model = Therapist
    template_name = "therapist/therapist_list.html"
    context_object_name = "therapists"


class TherapistCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = "accounts.can_create_therapist"
    model = Therapist
    fields = [
        "name",
        "email",
        "birthday",
        "phone_number",
        "gender",
        "specialities",
        "crm",
        "availability_hours",
        "availability_days",
        "rate",
        "fee",
        "photo",
        "contract_scan",
    ]
    template_name = "therapist/therapist_form.html"
    success_url = reverse_lazy("therapist_list")


class TherapistUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = "accounts.modify_therapist_information"
    model = Therapist
    fields = [
        "name",
        "email",
        "birthday",
        "phone_number",
        "gender",
        "specialities",
        "crm",
        "availability_hours",
        "availability_days",
        "rate",
        "fee",
        "photo",
        "contract_scan",
    ]
    template_name = "therapist/therapist_form.html"
    success_url = reverse_lazy("therapist_list")


class TherapistDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = "accounts.modify_therapist_information"
    model = Therapist
    template_name = "therapist/therapist_delete.html"
    success_url = reverse_lazy("therapist_list")


class TherapistDetailView(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = "accounts.can_view_therapist_info"
    model = Therapist
    template_name = "therapist/therapist_detail.html"
    context_object_name = "therapist"
