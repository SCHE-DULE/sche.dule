from django.db.models import Q
from datetime import datetime, timedelta
from django import forms

from .models import Client, Speciality, Therapist
from .models import Appointment, Room


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "client",
            "service",
            "therapist",
            "room",
            "appointment_date",
            "time_start",
            "duration",
            "status",
            "notes",
        ]

    client = forms.ModelChoiceField(
        queryset=Client.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Cliente",
    )

    therapist = forms.ModelChoiceField(
        queryset=Therapist.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Terapeuta",
    )

    service = forms.ModelChoiceField(
        queryset=Speciality.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Tipo de Tratamento",
    )

    room = forms.ModelChoiceField(
        queryset=Room.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Sala",
    )

    appointment_date = forms.DateField(
        widget=forms.DateInput(
            format="%Y-%m-%d",
            attrs={"class": "form-control", "type": "date"},
        ),
        label="Data do Atendimento",
    )

    time_start = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "id": "timepicker-start",
                "class": "form-control ui-timepicker-input",
                "autocomplete": "off",
                "placeholder": "HH:MM",
            }
        ),
        label="Hora de início do Atendimento",
        help_text="Selecione a hora",
    )

    duration = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "id": "timepicker-duration",
                "class": "form-control ui-timepicker-input",
                "autocomplete": "off",
                "placeholder": "HH:MM",
            }
        ),
        label="Duração do Atendimento",
        help_text="Selecione a duração",
    )

    status = forms.ChoiceField(
        choices=Appointment.STATUS_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Status",
    )

    notes = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        label="Observações",
        required=False,
    )

    def is_valid(self) -> bool:
        valid = super().is_valid()

        if not valid:
            return valid

        time_start = self.cleaned_data.get("time_start")
        duration = self.cleaned_data.get("duration")
        time_start = self.cleaned_data.get("time_start")
        appointment_date = self.cleaned_data.get("appointment_date")
        room = self.cleaned_data.get("room")

        if time_start and duration:
            time_start = datetime.strptime(time_start, "%H:%M")
            duration = datetime.strptime(duration, "%H:%M")
            end_time = time_start + timedelta(hours=duration.hour, minutes=duration.minute, seconds=duration.second)
            self.instance.time_end = end_time.strftime("%H:%M:%S")

            closing_time = datetime(time_start.year, time_start.month, time_start.day, 19, 0)

            if end_time > closing_time:
                self.add_error(None, "Não é possível marcar horário para após o fechamento.")
                return False

        overlapping_appointments = Appointment.objects.filter(
            Q(appointment_date=appointment_date)
            & ~Q(id=self.instance.id)
            & Q(
                Q(
                    time_start__lte=time_start,
                    time_end__gt=time_start,
                )
                | Q(
                    time_start__lt=self.instance.time_end,
                    time_end__gte=self.instance.time_end,
                )
                | Q(
                    time_start__gte=time_start,
                    time_end__lte=self.instance.time_end,
                )
            )
            & Q(room__name=room)
        )
        if overlapping_appointments.exists():
            self.add_error(None, "O horário já está ocupado por outro agendamento.\nPor favor, escolha outro.")
            return False

        return valid
