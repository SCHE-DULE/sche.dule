from typing import Any
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from .forms import AppointmentForm

from .models import Appointment

class AppointmentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "accounts.can_view_appointment_list"
    model = Appointment
    template_name = 'appointment/appointment_list.html'  
    context_object_name = 'appointments'
    extra_context = {
        'page_name': 'Agendamento', 
        'page_section': 'Lista',
        }
    ordering = ['appointment_date']


class AppointmentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "accounts.can_view_appointment_info"
    model = Appointment
    template_name = 'appointment/appointment_detail.html'  
    context_object_name = 'appointment'
    extra_context = {
        'page_name': 'Agendamento', 
        'page_section': 'Detalhes',
        }


class AppointmentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "accounts.can_create_appointment"
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointment/appointment_form.html'  
    extra_context = {
        'page_name': 'Agendamento', 
        'page_section': 'Cadastrar',
        }

    def get_success_url(self):
        return reverse_lazy("appointment-detail", kwargs={"pk": self.object.pk})


class AppointmentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "accounts.can_edit_appointment"
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointment/appointment_form.html'  
    extra_context = {
        'page_name': 'Agendamento', 
        'page_section': 'Atualizar',
        }

    def get_success_url(self):
        return reverse_lazy("appointment-detail", kwargs={"pk": self.object.pk})


class AppointmentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "accounts.can_remove_appointment"
    model = Appointment
    template_name = 'appointment/appointment_confirm_delete.html' 
    success_url = reverse_lazy("appointment-list")
    extra_context = {
        'page_name': 'Agendamento', 
        'page_section': 'Desativar',
        }
    
@login_required
def dashboard(request):
    appointments = Appointment.objects.order_by('appointment_date')
    
    extra_context = {
        'page_section': 'Dashboard',
    }
    
    return render(request, 'dashboard/dashboard.html', {'appointments': appointments, **extra_context})