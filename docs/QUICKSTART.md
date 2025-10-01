# Quick Start Guide

This guide will help you get the Debuttend CMS up and running quickly.

## Prerequisites

- Python 3.10 or higher
- PostgreSQL 15 or higher
- Git
- Docker (optional, for containerized setup)

## Option 1: Local Development (Traditional)

### 1. Clone the repository

```bash
git clone https://github.com/Ryangcastillo/dJango-Wagtail-CMS-backend.git
cd dJango-Wagtail-CMS-backend
```

### 2. Set up Python virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
# Edit .env with your settings
```

### 5. Set up the database

Make sure PostgreSQL is running, then:

```bash
cd debuttend_cms
python manage.py migrate
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Access the application at:
- **Wagtail Admin**: http://localhost:8000/cms/
- **Django Admin**: http://localhost:8000/django-admin/
- **Public Site**: http://localhost:8000/

## Option 2: Docker Development (Recommended)

### 1. Clone the repository

```bash
git clone https://github.com/Ryangcastillo/dJango-Wagtail-CMS-backend.git
cd dJango-Wagtail-CMS-backend
```

### 2. Start services with Docker Compose

```bash
docker compose up -d
```

### 3. Run migrations and create superuser

```bash
docker compose exec web python debuttend_cms/manage.py migrate
docker compose exec web python debuttend_cms/manage.py createsuperuser
```

### 4. Access the application

Visit http://localhost:8000

To view logs:
```bash
docker compose logs -f
```

To stop services:
```bash
docker compose down
```

## Initial Setup

### Create Initial Pages

1. Log in to Wagtail admin at http://localhost:8000/cms/
2. Go to Pages and create:
   - A `HomePage` at the site root
   - An `ArticlePage` under the home page (optional)
   - A `DashboardPage` with slug `dashboard`

### Configure Integrations

1. Go to Snippets → Integrations
2. Add your external service integrations
3. Configure API keys and credentials

### Set Up Dashboard Widgets

1. Go to Snippets → Dashboard Widgets
2. Create widgets for your dashboard
3. Add them to your Dashboard Page

## Development Workflow

### Running Tests

```bash
# Local
cd debuttend_cms
python manage.py test

# Docker
docker compose exec web python debuttend_cms/manage.py test
```

### Code Linting and Formatting

```bash
# Install ruff
pip install ruff

# Check code
ruff check .

# Format code
ruff format .

# Auto-fix issues
ruff check --fix .
```

### Creating Migrations

```bash
# Local
cd debuttend_cms
python manage.py makemigrations

# Docker
docker compose exec web python debuttend_cms/manage.py makemigrations
```

### Collecting Static Files

```bash
# Local
cd debuttend_cms
python manage.py collectstatic

# Docker
docker compose exec web python debuttend_cms/manage.py collectstatic
```

## CI/CD Setup

The project includes pre-configured CI/CD pipelines:

- **GitHub Actions**: `.github/workflows/ci.yml` and `.github/workflows/deploy.yml`
- **GitLab CI**: `.gitlab-ci.yml`

See [CI/CD Documentation](docs/CI_CD.md) for detailed setup instructions.

### Required Secrets for CI/CD

Configure these in your CI/CD platform:

- `DJANGO_SECRET_KEY`
- `DB_ENGINE`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`

## Deployment

### Docker Deployment

Build the production image:

```bash
docker build -t debuttend-cms:latest .
```

Run the container:

```bash
docker run -p 8000:8000 \
  -e DJANGO_SECRET_KEY=your-secret \
  -e DJANGO_DB_HOST=your-db-host \
  -e DJANGO_DB_NAME=your-db-name \
  -e DJANGO_DB_USER=your-db-user \
  -e DJANGO_DB_PASSWORD=your-db-password \
  debuttend-cms:latest
```

### Platform-Specific Deployment

The deployment workflow includes examples for:

- Heroku
- AWS Elastic Beanstalk
- Google Cloud Platform
- DigitalOcean
- Kubernetes

See `.github/workflows/deploy.yml` for configuration examples.

## Troubleshooting

### Database Connection Issues

- Ensure PostgreSQL is running
- Check database credentials in `.env`
- For Docker: Use `DJANGO_DB_HOST=db` instead of `localhost`

### Migration Errors

```bash
# Reset database (CAUTION: This will delete all data)
cd debuttend_cms
python manage.py flush
python manage.py migrate
```

### Static Files Not Loading

```bash
cd debuttend_cms
python manage.py collectstatic --clear --noinput
```

### Port Already in Use

```bash
# Find process using port 8000
lsof -i :8000

# Kill the process
kill -9 <PID>

# Or use a different port
python manage.py runserver 0.0.0.0:8001
```

## Next Steps

1. Read the [CI/CD Documentation](docs/CI_CD.md) for deployment setup
2. Configure your analytics integrations
3. Set up external service integrations
4. Customize page models for your needs
5. Configure production settings in `debuttend_cms/settings/prod.py`

## Useful Commands

```bash
# Create a new Django app
python manage.py startapp myapp

# Create a superuser
python manage.py createsuperuser

# Open Django shell
python manage.py shell

# Check for issues
python manage.py check

# Run development server on specific port
python manage.py runserver 0.0.0.0:8080

# View all available management commands
python manage.py help
```

## Support

For issues and questions:
- Check the [CI/CD Documentation](docs/CI_CD.md)
- Review Django documentation: https://docs.djangoproject.com/
- Review Wagtail documentation: https://docs.wagtail.org/

Happy coding! 🚀
