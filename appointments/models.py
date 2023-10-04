from django.db import models
from accounts.models import Client, Therapist, TimeSlot
from treatments.models import Speciality


class Appointment(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "Pendente"),
        ("CONFIRMED", "Confirmada"),
        ("CANCELLED", "Cancelada"),
        ("COMPLETED", "Concluída"),
    )

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="appointments",
        verbose_name="Cliente",
        blank=False,
        null=False,
    )
    therapist = models.ForeignKey(
        Therapist,
        on_delete=models.CASCADE,
        related_name="therapist_appointments",
        verbose_name="Terapeuta",
    )
    service = models.ForeignKey(
        Speciality,
        on_delete=models.CASCADE,
        related_name="service_appointments",
        verbose_name="Tipo de Tratamento",
    )

    appointment_date = models.DateField(
        verbose_name="Data do Atendimento",
        blank=False,
        null=False,
    )
    appointment_time_slot = models.ForeignKey(
        TimeSlot,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="time_slot_appointments",
        verbose_name="Horário do Atendimento",
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="PENDING",
        verbose_name="Status",
        blank=False,
        null=False,
    )
    notes = models.TextField(blank=True, null=True, verbose_name="Observações")

    def __str__(self):
        return f"Atendimento para {self.client.name} com {self.therapist.name} ({self.service.name}) em {self.appointment_date} às {self.appointment_time_slot}"

    class Meta:
        verbose_name = "Atendimento"
        verbose_name_plural = "Atendimentos"


class AppointmentPackage(models.Model):
    therapist = models.ForeignKey(
        Therapist,
        on_delete=models.CASCADE,
        related_name="appointment_packages",
        verbose_name="Terapeuta",
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Nome do Pacote",
        blank=False,
        null=False,
    )
    description = models.TextField(verbose_name="Observações")
    original_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Preço Original",
        blank=False,
        null=False,
    )
    discounted_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Preço com Desconto",
        blank=False,
        null=False,
    )
    appointments = models.ManyToManyField(Appointment, verbose_name="Atendimentos")

    def __str__(self):
        return f"Pacote: {self.name} - Terapeuta: {self.therapist.name}"

    class Meta:
        verbose_name = "Appointment Package"
        verbose_name_plural = "Appointment Packages"
