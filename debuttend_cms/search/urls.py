"""URL routing for search views."""
from __future__ import annotations

from django.urls import path

from .views import SearchView

app_name = "search"

urlpatterns = [
    path("", SearchView.as_view(), name="results"),
]
