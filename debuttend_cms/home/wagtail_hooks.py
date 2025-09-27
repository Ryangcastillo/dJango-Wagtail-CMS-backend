"""Custom Wagtail hooks for the Debuttend CMS."""
from __future__ import annotations

from wagtail import hooks
from wagtail.admin.menu import MenuItem
from django.urls import reverse


@hooks.register("register_admin_menu_item")
def register_integrations_menu_item():
    return MenuItem("Integrations", reverse("integrations:list"), icon_name="link", order=601)
