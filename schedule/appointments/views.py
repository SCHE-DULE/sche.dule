from datetime import datetime, timedelta
from pprint import pprint
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
import json

from schedule.accounts.models import TimeSlot
from schedule.treatments.models import Speciality
from .serializers import AppointmentSerializer
from helpers.decorators import ajax_required

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from .forms import AppointmentForm

from .models import Appointment, Room


class AppointmentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "accounts.can_view_appointment_list"
    model = Appointment
    template_name = "appointment/appointment_list.html"
    context_object_name = "appointments"
    extra_context = {
        "page_name": "Agendamento",
        "page_section": "Lista",
    }
    ordering = ["appointment_date"]
    paginate_by = 10


class AppointmentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "accounts.can_view_appointment_info"
    model = Appointment
    template_name = "appointment/appointment_detail.html"
    context_object_name = "appointment"
    extra_context = {
        "page_name": "Agendamento",
        "page_section": "Detalhes",
    }


class AppointmentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "accounts.can_create_appointment"
    model = Appointment
    form_class = AppointmentForm
    template_name = "appointment/appointment_form.html"
    extra_context = {
        "page_name": "Agendamento",
        "page_section": "Cadastrar",
    }

    def get_success_url(self):
        return reverse_lazy("appointment-detail", kwargs={"pk": self.object.pk})  # type: ignore


class AppointmentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "accounts.can_edit_appointment"
    model = Appointment
    form_class = AppointmentForm
    template_name = "appointment/appointment_form.html"
    extra_context = {
        "page_name": "Agendamento",
        "page_section": "Atualizar",
    }

    def get_initial(self):
        initial = super().get_initial()
        time_start = self.object.time_start  # type: ignore
        time_end = self.object.time_end  # type: ignore

        if time_start and time_end:
            time_end = datetime.combine(self.object.appointment_date, time_end)  # type: ignore
            duration = time_end - timedelta(
                hours=time_start.hour,
                minutes=time_start.minute,
                seconds=time_start.second,
            )
            initial["time_start"] = time_start
            initial["duration"] = duration.strftime("%H:%M")  # type: ignore

        return initial

    def get_success_url(self):
        return reverse_lazy("appointment-detail", kwargs={"pk": self.object.pk})  # type: ignore


class AppointmentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "accounts.can_remove_appointment"
    model = Appointment
    template_name = "appointment/appointment_confirm_delete.html"
    success_url = reverse_lazy("appointment-list")
    extra_context = {
        "page_name": "Agendamento",
        "page_section": "Desativar",
    }


@login_required
def dashboard(request):
    rooms = Room.objects.all()
    time_slots = TimeSlot.objects.all()
    specialities = Speciality.objects.all()
    extra_context = {
        "page_section": "Próximos Atendimentos",
        "rooms": rooms,
        "time_slots": time_slots,
        "specialities": specialities,
    }

    return render(request, "dashboard/dashboard.html", {**extra_context})


@ajax_required
@require_http_methods(["GET"])
@login_required
def get_appointment_data(request):
    id = request.GET.get("id")

    appointment = Appointment.objects.get(pk=id)
    serializer = AppointmentSerializer(appointment)

    response = JsonResponse({"appointment": serializer.data})
    response["X-CSRFToken"] = get_token(request)

    return response


@ajax_required
@require_POST
@login_required
def update_appointment_data(request):
    try:
        data = json.loads(request.body)
        pprint(data)
        id = data.get("id")
        start = data.get("start")
        end = data.get("end")
        roomId = data.get("roomId")
        serviceId = data.get("serviceId")
        date = data.get("date")

        appointment = Appointment.objects.get(pk=id)
        room = int(roomId)

        appointment.time_start = datetime.strptime(start, "%H:%M:%S").time()
        appointment.time_end = datetime.strptime(end, "%H:%M:%S").time()
        appointment.room = Room.objects.get(pk=room)

        if date:
            appointment.appointment_date = datetime.strptime(date, "%d/%m/%Y").date()
        if serviceId:
            appointment.service = Speciality.objects.get(pk=serviceId)

        appointment.save()

        serializer = AppointmentSerializer(appointment)

        response = JsonResponse({"appointment": serializer.data})
        response["X-CSRFToken"] = get_token(request)

        return response
    except Appointment.DoesNotExist:
        return JsonResponse({"error": "Appointment not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@login_required
@ajax_required
@require_http_methods(["GET"])
def get_dashboard_calendar(request):
    date = request.GET.get("date")
    date_obj = datetime.strptime(date, "%Y-%m-%d")

    upcoming_appointments = Appointment.objects.filter(
        appointment_date=date_obj
    ).order_by("appointment_date", "time_start")

    serializer = AppointmentSerializer(upcoming_appointments, many=True)

    response = JsonResponse({"appointments": serializer.data})
    response["X-CSRFToken"] = get_token(request)

    return response
