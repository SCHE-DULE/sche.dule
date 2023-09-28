from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from helpers.decorators import ajax_required

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from appointments.models import Appointment

from ..forms import TherapistForm

from ..models import Therapist

class TherapistListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "accounts.can_view_therapist_list"
    model = Therapist
    template_name = "therapist/therapist_list.html"
    context_object_name = "therapists"
    extra_context = {
        'page_name': 'Terapeutas', 
        'page_section': 'Lista',
        }


class TherapistCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "accounts.can_create_therapist"
    model = Therapist
    form_class = TherapistForm
    template_name = "therapist/therapist_form.html"
    success_url = reverse_lazy("therapist_list")
    extra_context = {
        'page_name': 'Terapeutas', 
        'page_section': 'Cadastrar',
        }


class TherapistUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "accounts.modify_therapist_information"
    model = Therapist
    form_class = TherapistForm
    template_name = "therapist/therapist_form.html"
    success_url = reverse_lazy("therapist_list")
    extra_context = {
        'page_name': 'Terapeutas', 
        'page_section': 'Atualizar',
        }


class TherapistDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "accounts.modify_therapist_information"
    model = Therapist
    template_name = "therapist/therapist_delete.html"
    success_url = reverse_lazy("therapist_list")
    extra_context = {
        'page_name': 'Terapeutas', 
        'page_section': 'Desativar',
        }


class TherapistDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "accounts.can_view_therapist_info"
    model = Therapist
    template_name = "therapist/therapist_detail.html"
    context_object_name = "therapist"
    extra_context = {
        'page_name': 'Terapeutas', 
        'page_section': 'Detalhes',
        }
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        therapist = self.get_object()
        appointments = Appointment.objects.filter(therapist=therapist)
        context['appointments'] = appointments
        return context
    
@login_required
@ajax_required
@require_http_methods(["GET"])
def get_therapists_by_speciality(request):
    speciality_id = request.GET.get('speciality_id')
    therapists = Therapist.objects.filter(specialities__id=speciality_id)
    therapist_list = [{'pk': therapist.pk, 'name': therapist.name} for therapist in therapists]
    return JsonResponse({'therapists': therapist_list})