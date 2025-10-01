# Python Best Practices Guide

This document outlines the Python best practices implemented in the Debuttend CMS project, inspired by the GitHub Spec-Kit guidelines.

## Project Structure

The project follows Django's recommended structure with clear separation of concerns:

```
dJango-Wagtail-CMS-backend/
├── debuttend_cms/              # Main Django project directory
│   ├── debuttend_cms/         # Core settings and configuration
│   │   ├── settings/          # Environment-specific settings
│   │   │   ├── base.py       # Shared base settings
│   │   │   ├── dev.py        # Development settings
│   │   │   ├── prod.py       # Production settings
│   │   │   └── test.py       # Test settings (SQLite)
│   │   ├── urls.py           # URL routing
│   │   ├── wsgi.py           # WSGI config
│   │   └── asgi.py           # ASGI config
│   ├── analytics/             # Analytics app
│   ├── dashboard/             # Dashboard app
│   ├── home/                  # Content/home app
│   ├── integrations/          # Integrations app
│   └── search/                # Search app
├── tests/                     # Centralized test directory
├── manage.py                  # Django management script
├── pyproject.toml            # Project metadata and dependencies
├── pytest.ini                # Pytest configuration
├── requirements.txt          # Production dependencies
└── README.md                 # Project documentation
```

## Configuration Management

### pyproject.toml

We use `pyproject.toml` as the single source of truth for:
- Project metadata
- Dependencies (production and development)
- Tool configurations (pytest, black, ruff, mypy)

Key benefits:
- Modern Python standard (PEP 518, PEP 621)
- Centralized configuration
- Better dependency management

### Environment-specific Settings

Django settings are split into:
- `base.py` - Shared settings for all environments
- `dev.py` - Development-specific settings
- `prod.py` - Production settings with security hardening
- `test.py` - Test settings (uses SQLite for faster tests)

## Testing Infrastructure

### Framework: pytest with pytest-django

We use pytest instead of Django's default unittest for:
- More concise test syntax
- Better fixtures and parametrization
- Extensive plugin ecosystem
- Better output formatting

### Test Organization

```
tests/
├── __init__.py                 # Test package init
├── conftest.py                # Shared fixtures and configuration
├── test_manage.py             # Tests for manage.py
├── test_settings.py           # Tests for settings modules
├── test_analytics.py          # Tests for analytics app
├── test_dashboard.py          # Tests for dashboard app
├── test_home.py               # Tests for home app
├── test_integrations.py       # Tests for integrations app
└── test_search.py             # Tests for search app
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=debuttend_cms

# Run specific test file
pytest tests/test_home.py

# Run tests with verbose output
pytest -v

# Run tests and show local variables on failure
pytest -l
```

### Test Database

Tests use SQLite in-memory database instead of PostgreSQL for:
- Faster test execution
- No external database dependencies
- Consistent test environment

## Code Quality Tools

### Black (Code Formatter)

```bash
# Format all Python files
black debuttend_cms/

# Check formatting without changes
black --check debuttend_cms/
```

Configuration in `pyproject.toml`:
- Line length: 100 characters
- Target version: Python 3.11+
- Excludes: migrations, build artifacts

### Ruff (Linter)

```bash
# Lint all Python files
ruff check debuttend_cms/

# Auto-fix issues
ruff check --fix debuttend_cms/
```

Checks for:
- Code style issues (pycodestyle)
- Common bugs (pyflakes)
- Import sorting (isort)
- Code complexity
- Security issues (flake8-bugbear)

### MyPy (Type Checker)

```bash
# Type check all Python files
mypy debuttend_cms/
```

Benefits:
- Catch type-related bugs early
- Better IDE support
- Self-documenting code

## Naming Conventions

### Files and Directories

- Use lowercase with underscores: `analytics_dashboard.py`
- Module names should be short and descriptive
- Test files: `test_*.py` or `*_test.py`

### Python Code

- Classes: `PascalCase` (e.g., `AnalyticsDashboardView`)
- Functions/methods: `snake_case` (e.g., `get_analytics_data`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_UPLOAD_SIZE`)
- Private attributes: `_leading_underscore` (e.g., `_internal_cache`)

### Django Specific

- Models: Singular nouns (e.g., `ArticlePage`, `DashboardWidget`)
- Apps: Plural nouns (e.g., `analytics`, `integrations`)
- Views: Descriptive with suffix (e.g., `AnalyticsDashboardView`)

## Import Organization

Imports should be organized in this order (separated by blank lines):

1. Standard library imports
2. Third-party imports (Django, Wagtail, etc.)
3. Local application imports

Example:
```python
from __future__ import annotations  # Always first for forward references

import os
from datetime import datetime
from pathlib import Path

from django.conf import settings
from django.db import models
from wagtail.models import Page

from home.models import HomePage
from integrations.utils import log_event
```

## Type Hints

Use type hints for function signatures:

```python
def get_analytics_data(
    start_date: datetime,
    end_date: datetime,
    user_id: int | None = None
) -> dict[str, Any]:
    """Retrieve analytics data for the specified period."""
    ...
```

## Documentation

### Docstrings

Use Google-style docstrings for modules, classes, and functions:

```python
def calculate_metrics(data: list[dict]) -> dict[str, float]:
    """Calculate key metrics from analytics data.
    
    Args:
        data: List of analytics data points.
        
    Returns:
        Dictionary containing calculated metrics.
        
    Raises:
        ValueError: If data is empty or invalid.
    """
    ...
```

### Comments

- Write comments for "why", not "what"
- Keep comments up-to-date with code changes
- Use TODO comments with owner: `# TODO(username): description`

## Git Practices

### .gitignore

Comprehensive patterns for:
- Python bytecode and caches
- Virtual environments
- Django-specific files (migrations, media, static)
- IDE configurations
- Environment files
- Test artifacts and coverage reports

## Continuous Integration

Recommended CI workflow steps:

1. Install dependencies
2. Run linters (ruff, black --check)
3. Run type checker (mypy)
4. Run tests with coverage (pytest --cov)
5. Upload coverage reports

## Key Improvements Made

### 1. Fixed "main.py" Issue

The project uses `manage.py` (Django standard), not `main.py`. Tests now verify:
- `manage.py` exists and is executable
- Management commands work correctly
- Django setup is valid

### 2. Testing Infrastructure

- Added pytest with pytest-django
- Created 21 tests covering all apps
- Test settings using SQLite for speed
- All tests passing

### 3. Fixed Import Issues

- Updated `Orderable` import (moved from modelcluster to wagtail.models)
- Fixed Wagtail API import (use `WagtailAPIRouter` instead of deprecated `API` class)

### 4. Project Configuration

- Added `pyproject.toml` with comprehensive configuration
- Updated `.gitignore` with Python best practices
- Added `pytest.ini` for test configuration
- Created test settings module

### 5. Documentation

- Updated README with testing instructions
- Added this best practices guide
- Improved code organization documentation

## Resources

- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Django Coding Style](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)
- [Wagtail Developer Documentation](https://docs.wagtail.org/en/stable/reference/)
- [pytest Documentation](https://docs.pytest.org/)
- [GitHub Spec-Kit](https://github.com/github/spec-kit)

## Next Steps

To further improve the project:

1. Set up CI/CD pipeline (GitHub Actions)
2. Add pre-commit hooks for code quality checks
3. Increase test coverage to 80%+
4. Add integration tests for API endpoints
5. Set up automated deployment
6. Add performance monitoring
7. Implement security scanning
