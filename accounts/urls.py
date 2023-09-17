from django.urls import path
from .views import (
    TherapistCreateView,
    TherapistDeleteView,
    TherapistDetailView,
    TherapistListView,
    TherapistUpdateView,
)


urlpatterns = [
    path("therapist/", TherapistListView.as_view(), name="therapist_list"),
    path("therapist/<int:pk>/", TherapistDetailView.as_view(), name="therapist_detail"),
    path("therapist/create/", TherapistCreateView.as_view(), name="therapist_create"),
    path(
        "therapist/<int:pk>/update/",
        TherapistUpdateView.as_view(),
        name="therapist_update",
    ),
    path(
        "therapist/<int:pk>/delete/",
        TherapistDeleteView.as_view(),
        name="therapist_delete",
    ),
]
