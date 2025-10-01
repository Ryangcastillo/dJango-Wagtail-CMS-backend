"""Tests for the integrations app."""
from __future__ import annotations

import pytest


@pytest.mark.django_db
class TestIntegrationsApp:
    """Test cases for the integrations app."""

    def test_integrations_app_config(self):
        """Test that the integrations app is configured correctly."""
        from integrations.apps import IntegrationsConfig

        assert IntegrationsConfig.name == "integrations"
        assert IntegrationsConfig.default_auto_field == "django.db.models.BigAutoField"
        assert IntegrationsConfig.verbose_name == "Integrations"

    def test_integrations_views_import(self):
        """Test that integrations views can be imported successfully."""
        try:
            from integrations import views  # noqa: F401

            assert True, "Integrations views imported successfully"
        except ImportError as e:
            pytest.fail(f"Failed to import integrations views: {e}")
