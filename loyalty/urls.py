from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('dashboard/', include('app.dashboards.urls')),
    path('accounts/', include('app.accounts.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]
