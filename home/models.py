"""Content models for the Debuttend CMS."""
from __future__ import annotations

from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, InlinePanel, ObjectList, TabbedInterface
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Orderable, Page, TranslatableMixin
from wagtail.search import index
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.snippets.models import register_snippet


class SEOFieldsMixin(models.Model):
    """Reusable SEO metadata fields for pages and snippets."""

    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)
    og_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    seo_panels = [
        FieldPanel("meta_title"),
        FieldPanel("meta_description"),
        FieldPanel("og_image"),
    ]

    class Meta:
        abstract = True


class HomePage(SEOFieldsMixin, Page):
    """Landing page with modular content blocks."""

    introduction = RichTextField(blank=True)
    body = StreamField(
        [
            (
                "hero",
                blocks.StructBlock(
                    [
                        ("heading", blocks.CharBlock(form_classname="full title")),
                        ("subheading", blocks.TextBlock(required=False)),
                        ("background_image", ImageChooserBlock(required=False)),
                        ("cta_text", blocks.CharBlock(required=False)),
                        ("cta_link", blocks.URLBlock(required=False)),
                    ],
                    template="home/blocks/hero_block.html",
                ),
            ),
            ("content", blocks.RichTextBlock(features=[
                "bold",
                "italic",
                "h2",
                "h3",
                "ol",
                "ul",
                "link",
                "image",
            ])),
            (
                "callout",
                blocks.StructBlock(
                    [
                        ("title", blocks.CharBlock()),
                        ("body", blocks.TextBlock()),
                        ("button_text", blocks.CharBlock(required=False)),
                        ("button_link", blocks.URLBlock(required=False)),
                    ],
                    template="home/blocks/callout_block.html",
                ),
            ),
        ],
        use_json_field=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("body"),
    ]

    promote_panels = Page.promote_panels + SEOFieldsMixin.seo_panels


class ArticlePage(SEOFieldsMixin, Page):
    """Flexible article page with modular StreamField content."""

    introduction = models.CharField(max_length=250, blank=True)
    featured_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="article_featured",
    )
    body = StreamField(
        [
            ("rich_text", blocks.RichTextBlock()),
            ("image", ImageChooserBlock()),
            (
                "quote",
                blocks.StructBlock(
                    [
                        ("quote", blocks.TextBlock()),
                        ("attribution", blocks.CharBlock(required=False)),
                    ],
                    template="home/blocks/quote_block.html",
                ),
            ),
            ("embed", blocks.URLBlock(help_text="Embed URL (YouTube, Vimeo, etc.)")),
        ],
        use_json_field=True,
        blank=True,
    )
    author = models.CharField(max_length=120, blank=True)
    published_date = models.DateField(null=True, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField("introduction"),
        index.SearchField("body"),
        index.SearchField("author"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("featured_image"),
        FieldPanel("author"),
        FieldPanel("published_date"),
        FieldPanel("body"),
    ]

    promote_panels = Page.promote_panels + SEOFieldsMixin.seo_panels


class DashboardWidget(TranslatableMixin, ClusterableModel):
    """Reusable dashboard widget snippets."""

    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    widget_type = models.CharField(
        max_length=50,
        choices=[
            ("stats", "Statistics"),
            ("chart", "Chart"),
            ("todo", "Task List"),
        ],
    )
    configuration = models.JSONField(default=dict, blank=True)

    panels = [
        FieldPanel("title"),
        FieldPanel("description"),
        FieldPanel("widget_type"),
        FieldPanel("configuration"),
    ]

    def __str__(self) -> str:  # pragma: no cover - human readable
        return self.title


register_snippet(DashboardWidget)


class DashboardPage(SEOFieldsMixin, Page):
    """Configurable dashboard page for editors."""

    subtitle = models.CharField(max_length=250, blank=True)
    layout = StreamField(
        [
            (
                "widget",
                blocks.StructBlock(
                    [
                        ("widget", SnippetChooserBlock(target_model=DashboardWidget)),
                        ("column_span", blocks.ChoiceBlock(
                            choices=[("1", "1 Column"), ("2", "2 Columns"), ("3", "3 Columns")],
                            default="1",
                        )),
                    ]
                ),
            ),
        ],
        use_json_field=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("layout"),
    ]
    promote_panels = Page.promote_panels + SEOFieldsMixin.seo_panels

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Content"),
            ObjectList(promote_panels, heading="Promote"),
            ObjectList(SEOFieldsMixin.seo_panels, heading="SEO"),
            ObjectList(Page.settings_panels, heading="Settings"),
        ]
    )


class Integration(TranslatableMixin, ClusterableModel):
    """Stores integration metadata and reusable connection details."""

    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    api_base_url = models.URLField()
    credential_key = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    last_synced_at = models.DateTimeField(null=True, blank=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("description"),
        FieldPanel("api_base_url"),
        FieldPanel("credential_key"),
        FieldPanel("is_active"),
        FieldPanel("last_synced_at"),
        InlinePanel("logs", label="Activity"),
    ]

    class Meta:
        verbose_name = "Integration"
        verbose_name_plural = "Integrations"
        unique_together = [('translation_key', 'locale')]

    def __str__(self) -> str:  # pragma: no cover
        return self.name


register_snippet(Integration)


class IntegrationLogEntry(Orderable):
    """Audit log for integration lifecycle events."""

    integration = ParentalKey(
        Integration,
        on_delete=models.CASCADE,
        related_name="logs",
    )
    status = models.CharField(
        max_length=20,
        choices=[("success", "Success"), ("error", "Error"), ("pending", "Pending")],
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    panels = [FieldPanel("status"), FieldPanel("message")]

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.integration.name} - {self.status}"
