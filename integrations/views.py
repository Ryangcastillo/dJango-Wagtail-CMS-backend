"""Views for managing integrations in the Debuttend CMS."""
from __future__ import annotations

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from home.models import Integration


class IntegrationListView(LoginRequiredMixin, ListView):
    template_name = "integrations/list.html"
    model = Integration
    context_object_name = "integrations"


class IntegrationDetailView(LoginRequiredMixin, DetailView):
    template_name = "integrations/detail.html"
    model = Integration
    context_object_name = "integration"

    def get_queryset(self):
        return super().get_queryset().prefetch_related("logs")
