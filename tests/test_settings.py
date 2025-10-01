"""Tests for Django settings configuration."""
from __future__ import annotations

import pytest


class TestSettings:
    """Test cases for Django settings."""

    def test_dev_settings_import(self):
        """Test that development settings can be imported."""
        try:
            from debuttend_cms.settings import dev  # noqa: F401

            assert True, "Development settings imported successfully"
        except ImportError as e:
            pytest.fail(f"Failed to import development settings: {e}")

    def test_base_settings_import(self):
        """Test that base settings can be imported."""
        try:
            from debuttend_cms.settings import base  # noqa: F401

            assert True, "Base settings imported successfully"
        except ImportError as e:
            pytest.fail(f"Failed to import base settings: {e}")

    def test_prod_settings_import(self):
        """Test that production settings can be imported."""
        try:
            from debuttend_cms.settings import prod  # noqa: F401

            assert True, "Production settings imported successfully"
        except ImportError as e:
            pytest.fail(f"Failed to import production settings: {e}")

    def test_settings_configuration(self):
        """Test that settings are properly configured."""
        from django.conf import settings

        assert hasattr(settings, "INSTALLED_APPS")
        assert hasattr(settings, "MIDDLEWARE")
        assert hasattr(settings, "ROOT_URLCONF")
        assert settings.ROOT_URLCONF == "debuttend_cms.urls"

    def test_wagtail_installed(self):
        """Test that Wagtail is in INSTALLED_APPS."""
        from django.conf import settings

        assert "wagtail" in settings.INSTALLED_APPS
        assert "wagtail.admin" in settings.INSTALLED_APPS
        assert "wagtail.api" in settings.INSTALLED_APPS

    def test_custom_apps_installed(self):
        """Test that custom apps are in INSTALLED_APPS."""
        from django.conf import settings

        # Check for custom apps
        custom_apps = ["home", "search", "dashboard", "integrations", "analytics"]
        for app in custom_apps:
            # Check if app name or its config is in INSTALLED_APPS
            assert any(
                app in installed_app for installed_app in settings.INSTALLED_APPS
            ), f"{app} should be in INSTALLED_APPS"
