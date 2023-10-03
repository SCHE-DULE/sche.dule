from django import forms

from accounts.models import Client, Speciality, Therapist, TimeSlot
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "client",
            "service",
            "therapist",
            "appointment_date",
            "appointment_time_slot",
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

    appointment_date = forms.DateField(
        widget=forms.DateInput(
            format=("%Y-%m-%d"), attrs={"class": "form-control", "type": "date"}
        ),
        label="Data do Atendimento",
    )

    appointment_time_slot = forms.ModelChoiceField(
        queryset=TimeSlot.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Horário do Atendimento",
        help_text="Selecione um horário para o agendamento",
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
