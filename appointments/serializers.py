from rest_framework import serializers

from accounts.serializers import (
    ClientSerializer,
    TherapistSerializer,
    TimeSlotSerializer,
)
from treatments.serializers import SpecialitySerializer
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    therapist = TherapistSerializer()
    service = SpecialitySerializer()
    appointment_time_slot = TimeSlotSerializer()
    appointment_service_color = serializers.CharField(
        source="service.treatment_type.color", read_only=True
    )

    class Meta:
        model = Appointment
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        custom_representation = {
            **representation,
            "appointment_service_color": representation["appointment_service_color"],
        }
        return custom_representation
