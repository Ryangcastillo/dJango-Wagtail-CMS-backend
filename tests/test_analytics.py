"""Tests for the analytics app."""
from __future__ import annotations

import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse

User = get_user_model()


@pytest.mark.django_db
class TestAnalyticsApp:
    """Test cases for the analytics app."""

    def test_analytics_app_config(self):
        """Test that the analytics app is configured correctly."""
        from analytics.apps import AnalyticsConfig

        assert AnalyticsConfig.name == "analytics"
        assert AnalyticsConfig.default_auto_field == "django.db.models.BigAutoField"
        assert AnalyticsConfig.verbose_name == "Analytics"

    def test_analytics_views_import(self):
        """Test that analytics views can be imported successfully."""
        try:
            from analytics import views  # noqa: F401

            assert True, "Analytics views imported successfully"
        except ImportError as e:
            pytest.fail(f"Failed to import analytics views: {e}")

    def test_analytics_dashboard_requires_login(self):
        """Test that analytics dashboard requires authentication."""
        client = Client()
        url = reverse("analytics:dashboard")
        response = client.get(url)
        # Should redirect to login
        assert response.status_code == 302
        assert "/login/" in response.url or "login" in response.url.lower()
