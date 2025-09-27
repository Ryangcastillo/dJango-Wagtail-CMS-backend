"""Analytics routes."""
from __future__ import annotations

from django.urls import path

from .views import AnalyticsDashboardView

app_name = "analytics"

urlpatterns = [
    path("", AnalyticsDashboardView.as_view(), name="dashboard"),
]
