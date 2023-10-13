from django.urls import path
from .views import (
    SpecialityListView,
    SpecialityDetailView,
    SpecialityCreateView,
    SpecialityUpdateView,
    SpecialityDeleteView,

    TreatmentTypeListView,
    TreatmentTypeDetailView,
    TreatmentTypeCreateView,
    TreatmentTypeUpdateView,
    TreatmentTypeDeleteView,
)

urlpatterns = [
    path('', SpecialityListView.as_view(), name='speciality_list'),
    path('<int:pk>/', SpecialityDetailView.as_view(), name='speciality_detail'),
    path('create/', SpecialityCreateView.as_view(), name='speciality_create'),
    path('<int:pk>/update/', SpecialityUpdateView.as_view(), name='speciality_update'),
    path('<int:pk>/delete/', SpecialityDeleteView.as_view(), name='speciality_delete'),

    path('treatment_type/', TreatmentTypeListView.as_view(), name='treatment_type_list'),
    path('treatment_type/<int:pk>/', SpecialityListView.as_view(), name='speciality_list_filtered'),
    path('treatment_type/create/', TreatmentTypeCreateView.as_view(), name='treatment_type_create'),
    path('treatment_type/update/<int:pk>/', TreatmentTypeUpdateView.as_view(), name='treatment_type_update'),
    path('treatment_type/delete/<int:pk>/', TreatmentTypeDeleteView.as_view(), name='treatment_type_delete'),
]
