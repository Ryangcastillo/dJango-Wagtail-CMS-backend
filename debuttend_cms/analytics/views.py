"""Analytics views leveraging mock data to outline dashboard behaviour."""
from __future__ import annotations

from datetime import datetime, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class AnalyticsDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "analytics/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.utcnow()
        context.update(
            {
                "traffic": [
                    {"date": (now - timedelta(days=idx)).strftime("%Y-%m-%d"), "visits": 120 + idx * 3}
                    for idx in range(7)
                ][::-1],
                "top_content": [
                    {"title": "Modular Content Strategies", "views": 523},
                    {"title": "Integrating APIs with Debuttend", "views": 412},
                    {"title": "Optimising CMS SEO", "views": 310},
                ],
                "system_health": {
                    "uptime": "99.99%",
                    "avg_response_time": "180ms",
                    "error_rate": "0.02%",
                },
            }
        )
        return context
