from django import forms
from .models import COLOR_CHOICES, Benefit, Speciality, TreatmentType

class SpecialityForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields = ['treatment_type', 'name', 'description', 'feature_img']

    treatment_type = forms.ModelChoiceField(
        queryset=TreatmentType.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Tipo de Tratamento'
    )

    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tratamento'}),
        label='Nome da Terapia'
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descrição do tratamento'}),
        label='Descrição',
        required=False
    )

    feature_img = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        label='Imagem de Destaque da Terapia'
    )

class TreatmentTypeForm(forms.ModelForm):
    class Meta:
        model = TreatmentType
        fields = ['name', 'color']

    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
        label='Tipo de Tratamento'
    )

    color = forms.ChoiceField(
        choices=COLOR_CHOICES,  
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Cor'
    )

class BenefitForm(forms.ModelForm):
    class Meta:
        model = Benefit
        fields = ['speciality', 'title', 'description']

    speciality = forms.ModelChoiceField(
        queryset=Speciality.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Especialidade'
    )

    title = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Título Benefício'
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        label='Descrição',
        required=False
    )