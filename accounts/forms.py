from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.safestring import mark_safe

from django import forms

from .models import Client, DayOfWeek, Speciality, SystemUser, Therapist, TimeSlot


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "email",
                "name": "email-username",
                "placeholder": "Insira seu username",
                "autofocus": True,
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password",
                "name": "password",
                "placeholder": mark_safe(
                    "&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;"
                ),
                "aria-describedby": "password",
            }
        )
    )


class SystemUserForm(forms.ModelForm):
    class Meta:
        model = SystemUser
        fields = [
            "name",
            "email",
            "birthday",
            "phone_number",
            "gender",
            "user_type",
            "photo",
        ]

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nome Completo",
            }
        ),
        label="Nome",
        help_text="Conforme documento",
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "name@example.com",
            }
        ),
        label="Email de Contato",
    )

    birthday = forms.DateField(
        widget=forms.DateInput(
            format=("%Y-%m-%d"), attrs={"class": "form-control", "type": "date"}
        ),
        label="Data de Nascimento",
    )

    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "(99) 99999-9999"}
        ),
        label="Número de Telefone",
    )

    gender = forms.ChoiceField(
        choices=SystemUser.GENDER_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Gênero",
    )

    user_type = forms.ChoiceField(
        choices=SystemUser.USER_TYPE,
        widget=forms.Select(
            attrs={
                "class": "form-select",
                "placeholder": "Selecione o tipo de usuário",
            }
        ),
        label="Tipo de Usuário",
    )

    photo = forms.ImageField(
        widget=forms.FileInput(
            attrs={"class": "form-control", "data-buttonText": "Find file"}
        ),
        label="Foto",
    )


class PasswordSetForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user_username = kwargs.pop("user_username", None)
        super().__init__(*args, **kwargs)

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        label="Password",
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        label="Confirm Password",
    )


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "name",
            "email",
            "birthday",
            "phone_number",
            "gender",
            "cpf",
            "rg_or_rne",
            "country",
            "state",
            "city",
            "neighborhood",
            "zip_code",
            "street_address",
            "number",
            "complement_address",
            "photo",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "name@example.com",
                },
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "name@example.com",
                }
            ),
            "birthday": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "class": "form-control",
                    "type": "date",
                },
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "(99) 99999-999",
                }
            ),
            "gender": forms.Select(
                attrs={
                    "class": "form-select",
                    "id": "exampleFormControlSelect1",
                    "aria-label": "Default select example",
                }
            ),
            "cpf": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "000.000.000-00",
                }
            ),
            "rg_or_rne": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "country": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "state": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "city": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "neighborhood": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "zip_code": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "street_address": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "number": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "complement_address": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "photo": forms.FileInput(
                attrs={
                    "class": "form-control",
                    "data-buttonText": "Find file",
                }
            ),
        }


class TherapistForm(forms.ModelForm):
    class Meta:
        model = Therapist
        fields = [
            "name",
            "email",
            "birthday",
            "phone_number",
            "gender",
            "crm",
            "availability_hours",
            "availability_days",
            "rate",
            "fee",
            "photo",
            "contract_scan",
            "specialities",
        ]

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nome Completo",
            }
        ),
        label="Nome",
        help_text="Conforme documento",
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "name@example.com",
            }
        ),
        label="Email de Contato",
    )

    birthday = forms.DateField(
        widget=forms.DateInput(
            format=("%Y-%m-%d"), attrs={"class": "form-control", "type": "date"}
        ),
        label="Data de Nascimento",
    )

    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "(99) 99999-9999"}
        ),
        label="Número de Telefone",
    )

    gender = forms.ChoiceField(
        choices=Therapist.GENDER_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Gênero",
    )

    crm = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Número do CRM",
            }
        ),
        label="CRM",
    )

    availability_hours = forms.ModelMultipleChoiceField(
        queryset=TimeSlot.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-select"}),
        label="Horários de Disponibilidade",
        help_text='Para selecionar vários, segure a tecla "SHIFT" enquanto seleciona',
    )

    availability_days = forms.ModelMultipleChoiceField(
        queryset=DayOfWeek.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-select"}),
        label="Dias de Disponibilidade",
        help_text='Para selecionar vários, segure a tecla "SHIFT" enquanto seleciona',
    )

    rate = forms.DecimalField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Valor",
                "aria-label": "Valor",
            }
        ),
        label="Valor da Consulta",
    )

    fee = forms.DecimalField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Valor",
                "aria-label": "Valor",
            }
        ),
        label="Taxa Administrativa",
    )

    photo = forms.ImageField(
        widget=forms.FileInput(
            attrs={"class": "form-control", "data-buttonText": "Find file"}
        ),
        label="Foto",
    )

    contract_scan = forms.FileField(
        widget=forms.FileInput(attrs={"class": "form-control"}),
        label="Digitalização de Contrato",
    )

    specialities = forms.ModelMultipleChoiceField(
        queryset=Speciality.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-select"}),
        label="Especialidades",
        help_text='Para selecionar vários, segure a tecla "SHIFT" enquanto seleciona',
    )
