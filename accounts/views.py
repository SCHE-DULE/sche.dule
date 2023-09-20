from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from .models import Client, Therapist
from .forms import ClientEditForm


class ClientListView(ListView):
    model = Client
    template_name = "client/client_list.html"
    context_object_name = "clients"


class ClientCreateView(CreateView):
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


class ClientUpdateView(UpdateView):
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


class ClientDeleteView(DeleteView):
    model = Client
    template_name = "client/client_confirm_delete.html"
    success_url = reverse_lazy("client_list")


class ClientDetailView(DetailView):
    model = Client
    template_name = "client/client_detail.html"
    context_object_name = "client"


class TherapistListView(ListView):
    model = Therapist
    template_name = "therapist/therapist_list.html"
    context_object_name = "therapists"


class TherapistCreateView(CreateView):
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


class TherapistUpdateView(UpdateView):
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


class TherapistDeleteView(DeleteView):
    model = Therapist
    template_name = "therapist/therapist_delete.html"
    success_url = reverse_lazy("therapist_list")


class TherapistDetailView(DetailView):
    model = Therapist
    template_name = "therapist/therapist_detail.html"
    context_object_name = "therapist"
