from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Organization, Subscription, SubscriptionPlan


@admin.register(Organization)
class OrganizationAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ["name", "created_on", "subscription_info"]
    search_fields = ["name"]

    def subscription_info(self, obj):
        try:
            subscription = Subscription.objects.get(organization=obj)
            return f"{subscription.plan} (Start: {subscription.start_date}, End: {subscription.end_date})"
        except Subscription.DoesNotExist:
            return "No subscription"

    subscription_info.short_description = "Subscription Information"


@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["organization", "plan", "start_date", "end_date", "active"]
    list_filter = ["plan", "active"]
    search_fields = ["organization__name", "plan__name"]
