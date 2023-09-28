from django import forms

from accounts.models import Client, Speciality, Therapist
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "client",
            "service",
            "therapist",
            "appointment_date_start",
            "appointment_date_end",
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

    appointment_date_start = forms.DateTimeField(
        widget=forms.DateTimeInput(
            format=("%Y-%m-%dT%H:%M"),
            attrs={"class": "form-control", "type": "datetime-local"},
        ),
        label="Data e Hora do início do Atendimento",
    )

    appointment_date_end = forms.DateTimeField(
        widget=forms.DateTimeInput(
            format=("%Y-%m-%dT%H:%M"),
            attrs={"class": "form-control", "type": "datetime-local"},
        ),
        label="Data e Hora do término do Atendimento",
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
