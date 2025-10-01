"""Search view implementation leveraging Wagtail's search backend."""
from __future__ import annotations

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View
from wagtail.models import Page


class SearchView(View):
    template_name = "search/results.html"
    paginate_by = 10

    def get(self, request, *args, **kwargs):  # noqa: D401 - standard Django signature
        """Handle GET requests by returning paginated search results."""
        query = request.GET.get("query", "").strip()
        if query:
            search_results = Page.objects.live().search(query)
        else:
            search_results = Page.objects.none()

        paginator = Paginator(search_results, self.paginate_by)
        page_number = request.GET.get("page")
        results_page = paginator.get_page(page_number)

        context = {
            "query": query,
            "results_page": results_page,
        }
        return render(request, self.template_name, context)
