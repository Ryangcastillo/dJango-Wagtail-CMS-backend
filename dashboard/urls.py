"""Dashboard routes."""
from __future__ import annotations

from django.urls import path

from .views import DashboardView

app_name = "dashboard"

urlpatterns = [
    path("", DashboardView.as_view(), name="index"),
]
