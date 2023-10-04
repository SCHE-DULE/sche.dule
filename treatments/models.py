from django.db import models

COLOR_CHOICES = [
    ("azul", "Azul"),
    ("indigo", "Indigo"),
    ("roxo", "Roxo"),
    ("rosa", "Rosa"),
    ("vermelho", "Vermelho"),
    ("laranja", "Laranja"),
    ("amarelo", "Amarelo"),
    ("verde", "Verde"),
    ("teal", "Teal"),
    ("ciano", "Ciano"),
    ("branco", "Branco"),
]


class Speciality(models.Model):
    treatment_type = models.ForeignKey(
        "TreatmentType", blank=True, null=True, on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=50,
        verbose_name="Nome do Tratamento",
        blank=False,
        null=False,
    )
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")
    feature_img = models.ImageField(
        upload_to="terapias/", verbose_name="Imagem de Destaque da Terapia"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Terapia"
        verbose_name_plural = "Terapias"


class TreatmentType(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Tipo de Tratamento",
        blank=False,
        null=False,
    )
    color = models.CharField(choices=COLOR_CHOICES, max_length=15, default="branco")

    class Meta:
        verbose_name = "Tipo de Tratamento"
        verbose_name_plural = "Tipos de Tratamento"

    def __str__(self):
        return self.name


class Benefit(models.Model):
    speciality = models.ForeignKey("Speciality", on_delete=models.CASCADE)
    title = models.CharField(
        max_length=50,
        verbose_name="Titulo Beneficio",
        blank=False,
        null=False,
    )
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")

    class Meta:
        verbose_name = "Benefício"
        verbose_name_plural = "Benefícios"

    def __str__(self):
        return self.title
