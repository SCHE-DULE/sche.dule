from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, AbstractUser, Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver


from .permissions import PERMISSIONS_MAP


class BaseUser(AbstractUser):
    GENDER_CHOICES = (
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("O", "Outro"),
    )

    name = models.CharField(
        max_length=255, null=None, verbose_name="Nome conforme documento"
    )
    email = models.EmailField(max_length=200, blank=False, null=False, unique=True)
    birthday = models.DateField(verbose_name="Data de aniversário")
    phone_number = models.CharField(max_length=20, verbose_name="Celular")
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, verbose_name="Gênero"
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name="Groups",
        blank=True,
        related_name="baseuser_groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="User Permissions",
        blank=True,
        related_name="baseuser_user_permissions",
    )

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"

    def save(self, *args, **kwargs):
        if not self.id:
            if (
                not User.objects.filter(username=self.email).exists()
                or User.objects.filter(username=self.name).exists()
            ):
                self.username = self.name.lower().replace(" ", "")

        super().save(*args, **kwargs)


class SystemUser(BaseUser):
    USER_TYPE = (
        ("RECEPTIONIST", "Recepcionista"),
        ("THERAPIST", "Terapeuta"),
        ("MANAGER", "Gerente"),
        ("GENERAL_MANAGER", "Gerente Geral"),
        ("ADMINISTRATOR", "Administrador"),
        ("SUPER_USER", "Super User"),
    )

    user_type = models.CharField(
        max_length=15, choices=USER_TYPE, verbose_name="Tipo de Usuário"
    )

    def save(self, *args, **kwargs):

        return super(SystemUser, self).save(*args, **kwargs)


    def assign_permissions(self):
        content_type = ContentType.objects.get_for_model(self)
        existing_permissions = Permission.objects.filter(content_type=content_type)

        for codename in PERMISSIONS_MAP.get(self.user_type, []):
            permission = existing_permissions.filter(codename=codename).first()

            if permission is None:
                permission = Permission.objects.create(
                    codename=codename,
                    content_type=content_type,
                    name=f"Can {codename.replace('_', ' ')} {self._meta.verbose_name}",
                )

            self.user_permissions.add(permission)

    class Meta:
        verbose_name = "Usuário do Sistema"
        verbose_name_plural = "Usuários do Sistema"


@receiver(post_save, sender=SystemUser)
def assign_groups_and_permissions(sender, instance, created, **kwargs):
    group, created = Group.objects.get_or_create(name=instance.user_type)

    print("Groups (Before Adding):", instance.groups.all())
    instance.groups.clear()
    instance.groups.add(group)

    print("Groups (After Adding):", instance.groups.all())

    instance.assign_permissions()
        

class Therapist(BaseUser):
    specialities = models.ManyToManyField("Speciality", verbose_name="Especialidades")
    crm = models.CharField(
        max_length=20, verbose_name="Cadastro do Órgão de Registro (ex: CRM)"
    )
    avaliability_days = models.CharField(
        max_length=100, verbose_name="Dias Disponíveis"
    )
    hours = models.CharField(max_length=100, verbose_name="Horário de Consulta")
    rate = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Valor Cobrado"
    )
    fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Taxa Administrativa (visível somente pelo gerente/administrador)",
        blank=True,
        null=True,
    )
    photo = models.ImageField(upload_to="terapeutas/", verbose_name="Foto do Terapeuta")
    contract_scan = models.FileField(
        upload_to="contratos/",
        verbose_name="Anexo do Contrato com o Terapeuta",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Terapeuta: {self.name}, Especialidades: {', '.join([speciality.name for speciality in self.specialities.all()])}, Registro: {self.crm}"

    class Meta:
        verbose_name = "Terapeuta"
        verbose_name_plural = "Terapeutas"


class Client(BaseUser):
    cpf = models.CharField(
        max_length=14, unique=True, verbose_name="CPF com validação de dígitos"
    )
    rg_or_rne = models.CharField(
        max_length=20,
        null=None,
        unique=True,
        verbose_name="RG ou RNE com validação de dígitos",
    )
    country = models.CharField(max_length=50, verbose_name="País")
    state = models.CharField(max_length=50, verbose_name="Estado")
    city = models.CharField(max_length=100, verbose_name="Cidade")
    neighborhood = models.CharField(max_length=100, verbose_name="Bairro")
    zip_code = models.CharField(max_length=100, verbose_name="CEP")
    street_address = models.CharField(max_length=255, verbose_name="Endereço")
    number = models.CharField(max_length=10, verbose_name="Número")
    complement_address = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Complemento"
    )
    observation = models.TextField(blank=True, null=True, verbose_name="Observação")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Speciality(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Speciality Name",
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Speciality"
        verbose_name_plural = "Specialities"
