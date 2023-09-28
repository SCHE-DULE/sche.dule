from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from ..models import SystemUser


class SystemUserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "accounts.manage_system_users"
    model = SystemUser
    template_name = "systemuser/systemuser_list.html"
    context_object_name = "systemusers"
    extra_context = {
        'page_name': 'Usuários', 
        'page_section': 'Lista',
        }


class SystemUserCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "accounts.manage_system_users"
    model = SystemUser
    fields = [
        "name",
        "email",
        "birthday",
        "phone_number",
        "gender",
        "user_type",
    ]
    template_name = "systemuser/systemuser_form.html"
    success_url = reverse_lazy("systemuser_list")
    extra_context = {
        'page_name': 'Usuários', 
        'page_section': 'Cadastro',
        }


class SystemUserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "accounts.manage_system_users"
    model = SystemUser
    fields = [
        "name",
        "email",
        "birthday",
        "phone_number",
        "gender",
        "user_type",
    ]
    template_name = "systemuser/systemuser_form.html"
    success_url = reverse_lazy("systemuser_list")
    extra_context = {
        'page_name': 'Usuário', 
        'page_section': 'Atualizar Informações',
        }


class SystemUserDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "accounts.manage_system_users"
    model = SystemUser
    template_name = "systemuser/systemuser_delete.html"
    success_url = reverse_lazy("systemuser_list")
    extra_context = {
        'page_name': 'Usuário', 
        'page_section': 'Desativar',
        }


class SystemUserDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "accounts.manage_system_users"
    model = SystemUser
    template_name = "systemuser/systemuser_detail.html"
    context_object_name = "systemuser"
    extra_context = {
        'page_name': 'Usuário', 
        'page_section': 'Detalhes',
        }
