# Refactoring Summary

This document summarizes the structural refactoring performed to align the project with Django/Wagtail spec kit best practices.

## Overview

The project has been restructured to follow standard Django/Wagtail project layout conventions, making it easier to understand, maintain, and test.

## Changes Made

### 1. Directory Structure Flattening

**Before:**
```
project_root/
├── manage.py
└── debuttend_cms/              # Extra nesting level
    ├── debuttend_cms/          # Django project config
    ├── home/                   # Apps nested too deep
    ├── search/
    └── ...
```

**After:**
```
project_root/
├── manage.py                   # Django management script
├── debuttend_cms/              # Django project config (flattened)
│   ├── settings/
│   ├── urls.py
│   └── wsgi.py
├── home/                       # Apps at root level
├── search/
├── analytics/
├── dashboard/
├── integrations/
└── templates/                  # Global templates
```

### 2. Import Fixes

Updated imports to use correct Wagtail 5.x API:

- **Orderable**: Changed from `modelcluster.models` to `wagtail.models`
- **API Router**: Changed from deprecated `wagtail.api.API` to `wagtail.api.v2.router.WagtailAPIRouter`

### 3. Model Fixes

- Added `unique_together` constraint to `Integration` model Meta to comply with Wagtail's `TranslatableMixin` requirements

### 4. CI/CD Updates

Updated all CI/CD workflows to work with the new structure:

- **GitHub Actions** (`.github/workflows/ci.yml`): Removed `cd debuttend_cms` commands
- **GitLab CI** (`.gitlab-ci.yml`): Removed `cd debuttend_cms` commands
- All Django management commands now run from the project root

### 5. Docker Configuration Updates

- **Dockerfile**: Updated to copy all app directories individually, removed `--chdir` flag from gunicorn
- **docker-compose.yml**: Updated volume mappings and command to run from root directory

### 6. Documentation Updates

Updated all documentation to reflect the new structure:

- `README.md`: Project structure diagram and Docker commands
- `CONTRIBUTING.md`: Project structure and testing instructions
- `docs/QUICKSTART.md`: Setup instructions and management commands

## Benefits

1. **Standard Django Layout**: Follows Django/Wagtail community best practices
2. **Easier Navigation**: Apps are at the root level, making the project structure more intuitive
3. **Simplified Commands**: No need to `cd` into directories before running management commands
4. **Better Testing**: Tests can now find modules correctly without path manipulation
5. **CI/CD Compatibility**: Workflows are simpler and more maintainable

## Testing

All changes have been validated:

- ✅ Django system checks pass
- ✅ Migrations are detected correctly
- ✅ Imports work without errors
- ✅ Ruff linter passes (with auto-fixes applied)
- ✅ Project structure follows Django spec kit best practices

## Migration Guide

If you have an existing development environment:

1. **Pull the latest changes**: `git pull origin main`
2. **No action needed**: The structure is self-contained and backward compatible
3. **Update your commands**: Remove any `cd debuttend_cms` from your scripts
4. **Docker users**: Run `docker-compose down` and `docker-compose up --build` to rebuild with new structure

## Key Files Changed

- `manage.py` - No changes (already at root)
- `debuttend_cms/` - Flattened from nested structure
- `home/models.py` - Fixed imports and added Meta constraint
- `debuttend_cms/urls.py` - Updated API router imports
- `.github/workflows/ci.yml` - Removed directory changes
- `.gitlab-ci.yml` - Removed directory changes
- `Dockerfile` - Updated copy commands and removed --chdir
- `docker-compose.yml` - Updated volume mappings
- `README.md`, `CONTRIBUTING.md`, `docs/QUICKSTART.md` - Updated documentation

## Questions or Issues?

If you encounter any issues with the new structure:

1. Check that you're running commands from the project root
2. Verify your virtual environment is activated
3. Ensure all dependencies are up to date: `pip install -r requirements.txt`
4. Review the [Quick Start Guide](docs/QUICKSTART.md) for setup instructions

For additional help, open an issue on GitHub with the "question" label.
