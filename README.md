# Debuttend CMS

Debuttend CMS is a modular, scalable content management system scaffold built with **Django** and **Wagtail**. The project emphasises a modern editorial experience, composable integrations, analytics, and a future-ready workflow that can support traditional, headless, or hybrid delivery models.

## Features

- **Wagtail-powered authoring** with StreamField-driven content blocks, SEO metadata, and reusable dashboard widgets.
- **Integration hub** that stores external service credentials, offers detail views for monitoring, and exposes an API-ready foundation.
- **Analytics dashboard** with interactive charts, top-performing content, and system health summaries.
- **Dashboard landing page** that editors can customise directly from Wagtail using reusable widget snippets.
- **REST API** powered by `wagtail.api` for headless or decoupled front-end integrations.
- **Environment aware settings** with `.env` support and production-ready security toggles.

## Project structure

```
debuttend_cms/
├── manage.py
├── debuttend_cms/
│   ├── debuttend_cms/
│   │   ├── settings/
│   │   │   ├── base.py
│   │   │   ├── dev.py
│   │   │   └── prod.py
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── home/
│   │   ├── models.py
│   │   └── templates/
│   ├── search/
│   ├── integrations/
│   ├── analytics/
│   └── dashboard/
└── requirements.txt
```

## Getting started

1. **Install dependencies**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure environment variables**

   Create a `.env` file at the repository root and add your credentials:

   ```dotenv
   DJANGO_SECRET_KEY=your-secret-key
   DJANGO_DEBUG=1
   DJANGO_DB_ENGINE=django.db.backends.postgresql
   DJANGO_DB_NAME=debuttend
   DJANGO_DB_USER=debuttend
   DJANGO_DB_PASSWORD=super-secret
   DJANGO_DB_HOST=localhost
   DJANGO_DB_PORT=5432
   ```

3. **Apply migrations & create a superuser**

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Run the development server**

   ```bash
   python manage.py runserver
   ```

5. **Access the CMS**

   - Wagtail admin: [http://localhost:8000/cms/](http://localhost:8000/cms/)
   - Django admin: [http://localhost:8000/django-admin/](http://localhost:8000/django-admin/)
   - Public site: [http://localhost:8000/](http://localhost:8000/)

6. **Seed initial pages**

   Within the Wagtail admin, create:

   - A `HomePage` instance at the site root.
   - An `ArticlePage` under the home page for sample content (optional).
   - A `DashboardPage` with the slug `dashboard` so that `/dashboard/` renders the editor-facing workspace.

## Content modelling overview

- `HomePage`: Flexible landing page with hero, rich content, and callout blocks.
- `ArticlePage`: StreamField-based article model with author metadata, scheduling, and SEO controls.
- `DashboardPage`: Editor-configurable dashboard that renders widget snippets on the public dashboard route.
- `DashboardWidget` (snippet): Reusable components for the dashboard layout.
- `Integration` (snippet) & `IntegrationLogEntry`: Persist integration credentials and audit logs for external services.

## API & headless readiness

The project enables `wagtail.api` and Django REST Framework by default. Content is available from `/api/v2/pages/`, providing a solid starting point for headless or decoupled front-end projects.

## Next steps

- Configure CI/CD pipelines (GitHub Actions, GitLab CI, etc.) to automate testing and deployment.
- Connect analytics to real data sources (Google Analytics, Plausible, etc.).
- Extend integrations with custom logic or webhook handlers.
- Implement advanced workflows like approval queues, content scheduling, and blue/green deployments.

---

This scaffold is intended to accelerate development of a fully featured CMS aligned with the Debuttend product vision. Customise, extend, and integrate as needed for your organisation.
