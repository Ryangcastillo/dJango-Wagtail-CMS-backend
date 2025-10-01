"""Tests for the dashboard app."""
from __future__ import annotations

import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse

User = get_user_model()


@pytest.mark.django_db
class TestDashboardApp:
    """Test cases for the dashboard app."""

    def test_dashboard_app_config(self):
        """Test that the dashboard app is configured correctly."""
        from dashboard.apps import DashboardConfig

        assert DashboardConfig.name == "dashboard"
        assert DashboardConfig.default_auto_field == "django.db.models.BigAutoField"
        assert DashboardConfig.verbose_name == "Dashboard"

    def test_dashboard_views_import(self):
        """Test that dashboard views can be imported successfully."""
        try:
            from dashboard import views  # noqa: F401

            assert True, "Dashboard views imported successfully"
        except ImportError as e:
            pytest.fail(f"Failed to import dashboard views: {e}")
