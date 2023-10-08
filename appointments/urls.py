from django.urls import path
from .views import (
    AppointmentListView,
    AppointmentDetailView,
    AppointmentCreateView,
    AppointmentUpdateView,
    AppointmentDeleteView,
    get_appointment_data,
    get_dashboard_calendar,
)

urlpatterns = [
    path('', AppointmentListView.as_view(), name='appointment-list'),
    path('<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
    path('create/', AppointmentCreateView.as_view(), name='appointment-create'),
    path('create/<int:service_pk>/', AppointmentCreateView.as_view(), name='appointment-create-treatment'),
    path('<int:pk>/update/', AppointmentUpdateView.as_view(), name='appointment-update'),
    path('<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment-delete'),
    path('get_dashboard_calendar/', get_dashboard_calendar, name='get_dashboard_calendar'),
    path('get_appointment_data/', get_appointment_data, name='get_appointment_data'),
]
