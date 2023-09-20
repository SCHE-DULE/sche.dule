from django.urls import path
from .views import (
    ClientListView,
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView,
    ClientDetailView,
    
    TherapistCreateView,
    TherapistDeleteView,
    TherapistDetailView,
    TherapistListView,
    TherapistUpdateView,
)


urlpatterns = [
    path("clients/", ClientListView.as_view(), name="client_list"),
    path("clients/create/", ClientCreateView.as_view(), name="client_create"),
    path("clients/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("clients/<int:pk>/update/", ClientUpdateView.as_view(), name="client_update"),
    path("clients/<int:pk>/delete/", ClientDeleteView.as_view(), name="client_delete"),

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
