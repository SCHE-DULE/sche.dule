from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from .models import Therapist


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
