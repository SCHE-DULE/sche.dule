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


class ClientListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "accounts.can_view_client_list"
    model = Client
    template_name = "client/client_list.html"
    context_object_name = "clients"


class ClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
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


class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
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


class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "accounts.modify_patient_information"
    model = Client
    template_name = "client/client_confirm_delete.html"
    success_url = reverse_lazy("client_list")


class ClientDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "accounts.can_view_client_info"
    model = Client
    template_name = "client/client_detail.html"
    context_object_name = "client"


class SystemUserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "accounts.manage_system_users"
    model = SystemUser
    template_name = "systemuser/systemuser_list.html"
    context_object_name = "systemusers"


class SystemUserCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
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


class SystemUserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
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


class SystemUserDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "accounts.manage_system_users"
    model = SystemUser
    template_name = "systemuser/systemuser_delete.html"
    success_url = reverse_lazy("systemuser_list")


class SystemUserDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "accounts.manage_system_users"
    model = SystemUser
    template_name = "systemuser/systemuser_detail.html"
    context_object_name = "systemuser"


class TherapistListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "accounts.can_view_therapist_list"
    model = Therapist
    template_name = "therapist/therapist_list.html"
    context_object_name = "therapists"


class TherapistCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
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


class TherapistUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
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


class TherapistDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "accounts.modify_therapist_information"
    model = Therapist
    template_name = "therapist/therapist_delete.html"
    success_url = reverse_lazy("therapist_list")


class TherapistDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "accounts.can_view_therapist_info"
    model = Therapist
    template_name = "therapist/therapist_detail.html"
    context_object_name = "therapist"
