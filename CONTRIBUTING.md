# Development Quick Start

Quick reference for developers working on Debuttend CMS.

## Setup

```bash
# Clone and setup
git clone https://github.com/Ryangcastillo/dJango-Wagtail-CMS-backend.git
cd dJango-Wagtail-CMS-backend

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -e ".[dev]"

# Setup environment
cp .env.example .env  # Edit with your settings

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

## Common Commands

### Django Management

```bash
# Run development server
python manage.py runserver

# Create new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Open Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic
```

### Testing

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_home.py

# Run with coverage
pytest --cov=debuttend_cms

# Run with verbose output
pytest -v

# Run and show local variables on failure
pytest -l --tb=short
```

### Code Quality

```bash
# Format code
black debuttend_cms/

# Check formatting
black --check debuttend_cms/

# Lint code
ruff check debuttend_cms/

# Fix linting issues automatically
ruff check --fix debuttend_cms/

# Type check
mypy debuttend_cms/
```

## Project Structure

```
debuttend_cms/          # Django apps live here
tests/                  # All tests go here
manage.py              # Django management script (NOT main.py!)
pyproject.toml         # Project configuration
pytest.ini             # Test configuration
requirements.txt       # Production dependencies
```

## URLs

- Development site: http://localhost:8000/
- Wagtail admin: http://localhost:8000/cms/
- Django admin: http://localhost:8000/django-admin/
- API: http://localhost:8000/api/v2/pages/
- Analytics: http://localhost:8000/analytics/
- Dashboard: http://localhost:8000/dashboard/

## Troubleshooting

### "No module named 'debuttend_cms.settings'"

Make sure you're in the project root directory and the virtual environment is activated.

### Tests failing with database errors

Tests use SQLite. Check that `debuttend_cms/debuttend_cms/settings/test.py` exists.

### Import errors with Wagtail

Ensure all dependencies are installed: `pip install -r requirements.txt`

## Getting Help

- Check [PYTHON_BEST_PRACTICES.md](PYTHON_BEST_PRACTICES.md) for coding standards
- Review [README.md](README.md) for project overview
- Open an issue on GitHub for bugs
- Refer to [Django docs](https://docs.djangoproject.com/) and [Wagtail docs](https://docs.wagtail.org/)
