from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accounts.forms import UserLoginForm

from .views import (
    ClientListView,
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView,
    ClientDetailView,

    SystemUserListView,
    SystemUserCreateView,
    SystemUserUpdateView,
    SystemUserDeleteView,
    SystemUserDetailView,
    
    TherapistCreateView,
    TherapistDeleteView,
    TherapistDetailView,
    TherapistListView,
    TherapistUpdateView,
)


urlpatterns = [

    path('login/', LoginView.as_view(
        authentication_form=UserLoginForm
        ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path("clients/", ClientListView.as_view(), name="client_list"),
    path("clients/create/", ClientCreateView.as_view(), name="client_create"),
    path("clients/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("clients/<int:pk>/update/", ClientUpdateView.as_view(), name="client_update"),
    path("clients/<int:pk>/delete/", ClientDeleteView.as_view(), name="client_delete"),

    path('systemusers/', SystemUserListView.as_view(), name='systemuser_list'),
    path('systemusers/create/', SystemUserCreateView.as_view(), name='systemuser_create'),
    path('systemusers/<int:pk>/', SystemUserDetailView.as_view(), name='systemuser_detail'),
    path('systemusers/<int:pk>/update/', SystemUserUpdateView.as_view(), name='systemuser_update'),
    path('systemusers/<int:pk>/delete/', SystemUserDeleteView.as_view(), name='systemuser_delete'),

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
