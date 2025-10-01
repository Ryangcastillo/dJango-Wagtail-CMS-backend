"""Tests for the search app."""
from __future__ import annotations

import pytest


@pytest.mark.django_db
class TestSearchApp:
    """Test cases for the search app."""

    def test_search_app_config(self):
        """Test that the search app is configured correctly."""
        from search.apps import SearchConfig

        assert SearchConfig.name == "search"
        assert SearchConfig.default_auto_field == "django.db.models.BigAutoField"

    def test_search_views_import(self):
        """Test that search views can be imported successfully."""
        try:
            from search import views  # noqa: F401

            assert True, "Search views imported successfully"
        except ImportError as e:
            pytest.fail(f"Failed to import search views: {e}")
