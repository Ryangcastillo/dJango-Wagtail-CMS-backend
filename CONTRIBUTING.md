# Contributing to Debuttend CMS

Thank you for your interest in contributing to Debuttend CMS! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/dJango-Wagtail-CMS-backend.git`
3. Set up your development environment (see [Quick Start Guide](docs/QUICKSTART.md))
4. Create a new branch: `git checkout -b feature/your-feature-name`

## Development Workflow

### Before Making Changes

1. Pull the latest changes from main:
   ```bash
   git checkout main
   git pull origin main
   ```

2. Create a new feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Making Changes

1. Write clean, readable code that follows the project's style
2. Add or update tests for your changes
3. Update documentation if needed
4. Commit your changes with clear, descriptive messages

### Code Quality

#### Linting

We use Ruff for code linting and formatting:

```bash
# Check code
ruff check .

# Format code
ruff format .

# Auto-fix issues
ruff check --fix .
```

#### Testing

Run tests before submitting your PR:

```bash
python manage.py test
```

#### Type Checking

Use type hints where appropriate:

```python
def my_function(name: str) -> str:
    return f"Hello, {name}"
```

### Commit Messages

Write clear commit messages:

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters
- Reference issues and pull requests where appropriate

Good examples:
```
Add user authentication feature
Fix bug in dashboard widget rendering
Update documentation for CI/CD setup
```

## Submitting Changes

### Pull Request Process

1. Push your changes to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. Go to the original repository on GitHub
3. Click "New Pull Request"
4. Select your fork and branch
5. Fill in the PR template with:
   - Description of changes
   - Related issue number (if applicable)
   - Screenshots (for UI changes)
   - Checklist of completed items

### PR Requirements

Before submitting, ensure:

- [ ] Code follows the project's style guidelines
- [ ] Tests pass locally
- [ ] Linting passes (ruff check)
- [ ] Documentation is updated (if needed)
- [ ] Commit messages are clear and descriptive
- [ ] No merge conflicts with main branch

### CI/CD Checks

Your PR will automatically trigger CI/CD workflows that check:

- **Tests**: All tests must pass
- **Linting**: Code must pass ruff checks
- **Security**: No security vulnerabilities detected
- **Migrations**: No missing migrations

## Code Style Guidelines

### Python Style

- Follow PEP 8 conventions
- Maximum line length: 120 characters
- Use double quotes for strings
- Use type hints for function parameters and return values
- Add docstrings for classes and functions

Example:
```python
from __future__ import annotations

from typing import Any

def process_data(data: dict[str, Any]) -> list[str]:
    """
    Process data and return a list of results.
    
    Args:
        data: Dictionary containing input data
        
    Returns:
        List of processed results
    """
    results = []
    # ... processing logic
    return results
```

### Django/Wagtail Style

- Use class-based views where appropriate
- Follow Django's model field ordering
- Use Wagtail's panels for admin configuration
- Keep models focused and single-purpose

Example:
```python
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


class MyPage(Page):
    """Custom page model."""
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]
    
    class Meta:
        verbose_name = "My Page"
```

## Project Structure

```
project_root/
├── manage.py            # Django management script
├── debuttend_cms/       # Django project settings
│   ├── settings/
│   │   ├── base.py      # Shared settings
│   │   ├── dev.py       # Development settings
│   │   └── prod.py      # Production settings
│   ├── urls.py          # URL configuration
│   └── wsgi.py          # WSGI configuration
├── home/                # Main content app
├── search/              # Search functionality
├── integrations/        # External integrations
├── analytics/           # Analytics dashboard
├── dashboard/           # Dashboard app
└── templates/           # Global templates
```

## Testing Guidelines

### Writing Tests

- Write tests for all new features
- Update tests when modifying existing features
- Use descriptive test names
- Test edge cases and error conditions

Example:
```python
from django.test import TestCase
from home.models import HomePage


class HomePageTestCase(TestCase):
    """Tests for HomePage model."""
    
    def setUp(self):
        """Set up test data."""
        self.home_page = HomePage.objects.create(
            title="Test Home",
            introduction="Test introduction"
        )
    
    def test_homepage_creation(self):
        """Test that a HomePage can be created."""
        self.assertIsNotNone(self.home_page)
        self.assertEqual(self.home_page.title, "Test Home")
```

### Running Tests

```bash
# Run all tests
python manage.py test

# Run tests for a specific app
python manage.py test home

# Run a specific test case
python manage.py test home.tests.HomePageTestCase

# Run with verbose output
python manage.py test --verbosity=2
```

## Documentation

### When to Update Documentation

- Adding new features
- Changing existing functionality
- Updating dependencies
- Modifying deployment processes

### Documentation Files

- `README.md`: Project overview and quick links
- `docs/QUICKSTART.md`: Getting started guide
- `docs/CI_CD.md`: CI/CD setup and usage
- `CONTRIBUTING.md`: This file

## Reporting Issues

### Bug Reports

When reporting bugs, include:

1. Description of the issue
2. Steps to reproduce
3. Expected behavior
4. Actual behavior
5. Environment details (OS, Python version, etc.)
6. Error messages or logs

### Feature Requests

For feature requests, describe:

1. The problem you're trying to solve
2. Proposed solution
3. Alternative solutions considered
4. Additional context

## Code Review Process

1. Maintainers will review your PR
2. Respond to feedback and make requested changes
3. Once approved, your PR will be merged
4. Your contribution will be acknowledged

## Community Guidelines

- Be respectful and inclusive
- Provide constructive feedback
- Help others when possible
- Follow the code of conduct

## Questions?

If you have questions:

- Check the documentation
- Search existing issues
- Open a new issue with the "question" label

Thank you for contributing to Debuttend CMS! 🎉
