from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from accounts.models import Therapist
from appointments.models import Appointment
from .forms import SpecialityForm, TreatmentTypeForm
from .models import Speciality, TreatmentType
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class SpecialityListView(ListView):
    model = Speciality
    template_name = "speciality/speciality_list.html"
    context_object_name = "specialities"
    extra_context = {
        "page_section": "Terapias",
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        treatments = TreatmentType.objects.all()
        selected_treatment_type_pk = self.kwargs.get("pk")

        treatment_list = []
        for treatment in treatments:
            treatment_list.append({"pk": treatment.pk, "name": treatment.name})
            if treatment.pk == selected_treatment_type_pk:
                context["selected_treatment_type_name"] = treatment.name

        context["treatment_type"] = treatment_list
        context["selected_treatment_type_pk"] = selected_treatment_type_pk
        return context

    def get_queryset(self):
        treatment_type_pk = self.kwargs.get("pk")
        print(self.kwargs.get("pk"))

        if treatment_type_pk is not None and treatment_type_pk != 0:
            return Speciality.objects.filter(treatment_type__pk=treatment_type_pk)
        else:
            return Speciality.objects.all()


class SpecialityDetailView(DetailView):
    model = Speciality
    template_name = "speciality/speciality_detail.html"
    context_object_name = "speciality"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["page_name"] = "Terapias"
        context["page_section"] = self.object.name  # type: ignore

        therapists = Therapist.objects.filter(specialities=self.object)  # type: ignore

        context["therapists"] = therapists

        appointments = Appointment.objects.filter(service=self.object)  # type: ignore

        context["appointments"] = appointments

        return context


class SpecialityCreateView(LoginRequiredMixin, CreateView):
    model = Speciality
    form_class = SpecialityForm
    template_name = "speciality/speciality_form.html"


class SpecialityUpdateView(LoginRequiredMixin, UpdateView):
    model = Speciality
    form_class = SpecialityForm
    template_name = "speciality/speciality_form.html"


class SpecialityDeleteView(LoginRequiredMixin, DeleteView):
    model = Speciality
    template_name = "speciality/speciality_confirm_delete.html"
    success_url = reverse_lazy("speciality_list")


class TreatmentTypeListView(ListView):
    model = TreatmentType
    template_name = "treatment_type/treatment_type_list.html"
    context_object_name = "treatment_type_list"


class TreatmentTypeDetailView(DetailView):
    model = TreatmentType
    template_name = "treatment_type/treatment_type_detail.html"
    context_object_name = "treatment_type"


class TreatmentTypeCreateView(CreateView):
    model = TreatmentType
    form_class = TreatmentTypeForm
    template_name = "treatment_type/treatment_type_form.html"
    success_url = reverse_lazy("treatment_type_list")


class TreatmentTypeUpdateView(UpdateView):
    model = TreatmentType
    form_class = TreatmentTypeForm
    template_name = "treatment_type/treatment_type_form.html"
    context_object_name = "treatment_type"
    success_url = reverse_lazy("treatment_type_list")


class TreatmentTypeDeleteView(DeleteView):
    model = TreatmentType
    template_name = "treatment_type/treatment_type_confirm_delete.html"
    context_object_name = "treatment_type"
    success_url = reverse_lazy("treatment_type_list")
