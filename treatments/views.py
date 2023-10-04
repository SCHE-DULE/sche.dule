from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from .models import Speciality, TreatmentType
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class SpecialityListView(ListView):
    model = Speciality
    template_name = "speciality/speciality_list.html"
    context_object_name = "specialities"
    extra_context = {
        'page_section': 'Terapias',
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


class SpecialityCreateView(LoginRequiredMixin, CreateView):
    model = Speciality
    template_name = "speciality/speciality_form.html"
    fields = ["name", "description", "feature_img"]


class SpecialityUpdateView(LoginRequiredMixin, UpdateView):
    model = Speciality
    template_name = "speciality/speciality_form.html"
    fields = ["name", "description", "feature_img"]


class SpecialityDeleteView(LoginRequiredMixin, DeleteView):
    model = Speciality
    template_name = "speciality/speciality_confirm_delete.html"
    success_url = reverse_lazy("speciality_list")
