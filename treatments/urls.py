from django.urls import path
from .views import (
    SpecialityListView,
    SpecialityDetailView,
    SpecialityCreateView,
    SpecialityUpdateView,
    SpecialityDeleteView,
)

urlpatterns = [
    path('', SpecialityListView.as_view(), name='speciality_list'),
    path('treatment_type/<int:pk>/', SpecialityListView.as_view(), name='speciality_list_filtered'),
    path('<int:pk>/', SpecialityDetailView.as_view(), name='speciality_detail'),
    path('create/', SpecialityCreateView.as_view(), name='speciality_create'),
    path('<int:pk>/update/', SpecialityUpdateView.as_view(), name='speciality_update'),
    path('<int:pk>/delete/', SpecialityDeleteView.as_view(), name='speciality_delete'),
]
