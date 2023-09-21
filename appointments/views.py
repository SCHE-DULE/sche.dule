from typing import Any
from django.http import HttpRequest
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from .models import Appointment

class AppointmentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "accounts.can_view_appointment_list"
    model = Appointment
    template_name = 'appointment/appointment_list.html'  
    context_object_name = 'appointments'


class AppointmentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "accounts.can_view_appointment_info"
    model = Appointment
    template_name = 'appointment/appointment_detail.html'  
    context_object_name = 'appointment'


class AppointmentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "accounts.can_create_appointment"
    model = Appointment
    template_name = 'appointment/appointment_form.html'  
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("appointment-detail", kwargs={"pk": self.object.pk})


class AppointmentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "accounts.can_edit_appointment"
    model = Appointment
    template_name = 'appointment/appointment_form.html'  
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("appointment-detail", kwargs={"pk": self.object.pk})


class AppointmentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "accounts.can_remove_appointment"
    model = Appointment
    template_name = 'appointment/appointment_confirm_delete.html' 
    success_url = reverse_lazy("appointment_list")