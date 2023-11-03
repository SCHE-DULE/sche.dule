from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from schedule.appointments.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('perfil/', include('finance.perfil.urls')),
    path('extrato/', include('finance.extrato.urls')),
    path('planejamento/', include('finance.planejamento.urls')),
    path('contas/', include('finance.contas.urls')),
    path('accounts/', include('schedule.accounts.urls')),
    path('appointments/', include('schedule.appointments.urls')),
    path('treatments/', include('schedule.treatments.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
