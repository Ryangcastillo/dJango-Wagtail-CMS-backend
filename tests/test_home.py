"""Tests for the home app models and functionality."""
from __future__ import annotations

import pytest
from django.test import TestCase


@pytest.mark.django_db
class TestHomeApp:
    """Test cases for the home app."""

    def test_home_app_config(self):
        """Test that the home app is configured correctly."""
        from home.apps import HomeConfig

        assert HomeConfig.name == "home"
        assert HomeConfig.default_auto_field == "django.db.models.BigAutoField"
        assert HomeConfig.verbose_name == "Content"

    def test_home_models_import(self):
        """Test that home models can be imported successfully."""
        try:
            from home import models  # noqa: F401

            assert True, "Home models imported successfully"
        except ImportError as e:
            pytest.fail(f"Failed to import home models: {e}")
