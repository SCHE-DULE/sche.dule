from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Organization(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)

    auto_create_schema = True

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"

class Domain(DomainMixin):
    pass


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Subscription Plan"
        verbose_name_plural = "Subscriptions Plans"


class Subscription(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    plan = models.ForeignKey(
        SubscriptionPlan, on_delete=models.CASCADE
    )  # TODO Create plans in create basic values
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.organization} - {self.plan}"

    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"
