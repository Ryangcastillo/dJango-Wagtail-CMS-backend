"""Dashboard view powered by the DashboardPage Wagtail model."""
from __future__ import annotations

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views import View
from wagtail.models import Site

from home.models import DashboardPage


class DashboardView(LoginRequiredMixin, View):
    template_name = "dashboard/index.html"

    def get(self, request, *args, **kwargs):
        site = Site.find_for_request(request)
        if site is None:
            site = Site.objects.order_by("-is_default_site").first()
        if site is None:
            raise Http404("No Wagtail site configured.")
        dashboard_page = get_object_or_404(
            DashboardPage,
            slug="dashboard",
            path__startswith=site.root_page.path,
        )
        return render(request, self.template_name, {"page": dashboard_page})
