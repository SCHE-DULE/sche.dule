from rest_framework import serializers

from .models import Client, Therapist, TimeSlot


class TherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = "__all__"
