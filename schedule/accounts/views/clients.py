from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from ..forms import ClientForm

from ..models import Client

class ClientListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "accounts.can_view_client_list"
    model = Client
    template_name = "client/client_list.html"
    context_object_name = "clients"
    extra_context = {
        'page_name': 'Clientes', 
        'page_section': 'Lista',
        }


class ClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "accounts.can_create_client"
    model = Client
    template_name = "client/client_form.html"
    form_class = ClientForm
    extra_context = {
        'page_name': 'Clientes', 
        'page_section': 'Cadastrar',
        }
    
    def get_success_url(self):
        return reverse_lazy("client_detail", kwargs={"pk": self.object.pk})


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
    extra_context = {
        'page_name': 'Clientes', 
        'page_section': 'Atualizar',
        }

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        user = self.request.user
        if not user.has_perm("accounts.modify_patient_information"): # type: ignore
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
    extra_context = {
        'page_name': 'Clientes', 
        'page_section': 'Desativar',
        }


class ClientDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "accounts.can_view_client_info"
    model = Client
    template_name = "client/client_detail.html"
    context_object_name = "client"
    extra_context = {
        'page_name': 'Clientes', 
        'page_section': 'Detalhes',
        }