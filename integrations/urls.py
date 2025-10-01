"""Integration routes."""
from __future__ import annotations

from django.urls import path

from .views import IntegrationDetailView, IntegrationListView

app_name = "integrations"

urlpatterns = [
    path("", IntegrationListView.as_view(), name="list"),
    path("<int:pk>/", IntegrationDetailView.as_view(), name="detail"),
]
