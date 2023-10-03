from typing import Any
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import FormView
from django.contrib import messages

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from accounts.forms import PasswordSetForm, SystemUserForm

from ..models import SystemUser


class SystemUserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "accounts.manage_system_users"
    model = SystemUser
    template_name = "systemuser/systemuser_list.html"
    context_object_name = "systemusers"
    extra_context = {
        "page_name": "Usuários",
        "page_section": "Lista",
    }


class SystemUserCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "accounts.manage_system_users"
    model = SystemUser
    form_class = SystemUserForm
    template_name = "systemuser/systemuser_form.html"
    success_url = reverse_lazy("systemuser_list")
    extra_context = {
        "page_name": "Usuários",
        "page_section": "Cadastro"
    }

    def get_success_url(self):
        return reverse_lazy("set_password", kwargs={"pk": self.object.pk})


class SystemUserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "accounts.manage_system_users"
    model = SystemUser
    form_class = SystemUserForm
    template_name = "systemuser/systemuser_form.html"
    success_url = reverse_lazy("systemuser_list")
    extra_context = {
        "page_name": "Usuário",
        "page_section": "Atualizar Informações",
    }

    def get_success_url(self):
        return reverse_lazy("systemuser_detail", kwargs={"pk": self.object.pk})


class SystemUserDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "accounts.manage_system_users"
    model = SystemUser
    template_name = "systemuser/systemuser_delete.html"
    success_url = reverse_lazy("systemuser_list")
    extra_context = {
        "page_name": "Usuário",
        "page_section": "Desativar",
    }


class SystemUserDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "accounts.manage_system_users"
    model = SystemUser
    template_name = "systemuser/systemuser_detail.html"
    context_object_name = "systemuser"
    extra_context = {
        "page_name": "Usuário",
        "page_section": "Detalhes",
    }


class PasswordSetView(LoginRequiredMixin, FormView):
    template_name = "registration/set_password.html"
    form_class = PasswordSetForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = SystemUser.objects.get(pk=self.kwargs["pk"])
        context["user_username"] = user.username 
        return context

    def get_success_url(self):
        return reverse_lazy("systemuser_detail", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        password = form.cleaned_data.get("password")
        confirm_password = form.cleaned_data.get("confirm_password")

        if password != confirm_password:
            form.add_error("confirm_password", "As senhas precisam ser iguais.")
            return self.form_invalid(form)

        user = SystemUser.objects.get(pk=self.kwargs["pk"])
        user.set_password(password)
        user.save()
        if user.check_password(password):
            messages.success(self.request, "Senha cadastrada com sucesso!")
        else:
            return self.form_invalid(form)

        return super().form_valid(form)
