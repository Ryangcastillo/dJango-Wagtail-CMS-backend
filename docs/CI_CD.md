# CI/CD Documentation

This document describes the Continuous Integration and Continuous Deployment (CI/CD) pipelines configured for the Debuttend CMS project.

## Overview

The project includes CI/CD configurations for both GitHub Actions and GitLab CI, providing flexibility for different hosting platforms.

## GitHub Actions

### Workflows

#### 1. CI Workflow (`.github/workflows/ci.yml`)

Runs on every push to `main` or `develop` branches and on all pull requests.

**Jobs:**
- **Test**: Runs the Django test suite across Python 3.10, 3.11, and 3.12
  - Sets up PostgreSQL service
  - Runs Django system checks
  - Checks for missing migrations
  - Runs all tests

- **Lint**: Code quality checks using Ruff
  - Runs linter to catch code issues
  - Checks code formatting

- **Security**: Security vulnerability scanning
  - Dependency vulnerability checks with Safety
  - Security linting with Bandit
  - Django deployment security checks

#### 2. Deploy Workflow (`.github/workflows/deploy.yml`)

Handles deployments to staging and production environments.

**Trigger Options:**
- Manual trigger via workflow dispatch
- Automatic on version tags (e.g., `v1.0.0`)

**Features:**
- Environment-specific deployments
- Static file collection
- Deployment status notifications
- Platform-agnostic (includes commented examples for various platforms)

### Setup Instructions

1. **Required Secrets** (Settings → Secrets → Actions):
   ```
   DJANGO_SECRET_KEY
   DB_ENGINE
   DB_NAME
   DB_USER
   DB_PASSWORD
   DB_HOST
   DB_PORT
   ```

2. **Optional Secrets** (depending on deployment platform):
   - Heroku: `HEROKU_API_KEY`, `HEROKU_APP_NAME`, `HEROKU_EMAIL`
   - AWS: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`
   - GCP: `GCP_CREDENTIALS`
   - DigitalOcean: `DIGITALOCEAN_ACCESS_TOKEN`
   - Docker: `DOCKER_USERNAME`, `DOCKER_PASSWORD`

3. **Environments**:
   - Create `staging` and `production` environments in Settings → Environments
   - Configure protection rules as needed

## GitLab CI

### Configuration (`.gitlab-ci.yml`)

**Stages:**
1. **Test**: Run tests with multiple Python versions
2. **Lint**: Code quality checks
3. **Security**: Security scanning
4. **Deploy**: Deployment to staging/production

**Features:**
- PostgreSQL service integration
- Multi-version Python testing
- Manual deployment triggers
- Environment-specific configurations

### Setup Instructions

1. **Variables** (Settings → CI/CD → Variables):
   ```
   DJANGO_SECRET_KEY
   DB_ENGINE
   DB_NAME
   DB_USER
   DB_PASSWORD
   DB_HOST
   DB_PORT
   ```

2. **Environments**:
   - Configure staging and production environments
   - Set environment URLs

## Docker Support

### Dockerfile

A multi-stage Dockerfile is provided for production deployments:

**Features:**
- Optimized layer caching
- Non-root user execution
- Health checks
- Gunicorn WSGI server

**Build:**
```bash
docker build -t debuttend-cms:latest .
```

**Run:**
```bash
docker run -p 8000:8000 \
  -e DJANGO_SECRET_KEY=your-secret \
  -e DJANGO_DB_HOST=db-host \
  debuttend-cms:latest
```

### Docker Compose

For local development and testing:

```bash
# Start services
docker-compose up -d

# Run migrations
docker-compose exec web python debuttend_cms/manage.py migrate

# Create superuser
docker-compose exec web python debuttend_cms/manage.py createsuperuser

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## Code Quality

### Ruff

Configuration in `pyproject.toml`:
- Line length: 120 characters
- Python 3.10+ target
- Django-specific rules enabled
- Import sorting with isort

**Local usage:**
```bash
# Check code
ruff check .

# Format code
ruff format .

# Auto-fix issues
ruff check --fix .
```

## Deployment Platforms

### Supported Platforms

The deployment workflow includes examples for:

1. **Heroku**
   - Uses `heroku-deploy` action
   - Automatic buildpack detection

2. **AWS Elastic Beanstalk**
   - Deploy with `beanstalk-deploy` action
   - Multi-environment support

3. **Google Cloud Platform**
   - App Engine deployment
   - Credentials-based auth

4. **DigitalOcean App Platform**
   - doctl integration
   - Container-based deployment

5. **Docker/Kubernetes**
   - Build and push Docker images
   - Deploy to any Kubernetes cluster

### Custom Deployment

To add your deployment platform:

1. Uncomment and customize the relevant section in `.github/workflows/deploy.yml`
2. Add required secrets in GitHub Settings
3. Test with manual trigger before enabling automatic deployments

## Testing Locally

### Run CI Checks Locally

**Tests:**
```bash
cd debuttend_cms
python manage.py test
```

**Linting:**
```bash
ruff check .
ruff format --check .
```

**Security:**
```bash
pip install safety bandit
safety check
bandit -r debuttend_cms/
```

**Django Checks:**
```bash
cd debuttend_cms
python manage.py check --deploy
```

## Environment Variables

### Required for CI/CD

| Variable | Description | Example |
|----------|-------------|---------|
| `DJANGO_SECRET_KEY` | Django secret key | Long random string |
| `DJANGO_DEBUG` | Debug mode | 0 for production |
| `DJANGO_DB_ENGINE` | Database engine | `django.db.backends.postgresql` |
| `DJANGO_DB_NAME` | Database name | `debuttend` |
| `DJANGO_DB_USER` | Database user | `debuttend` |
| `DJANGO_DB_PASSWORD` | Database password | Secure password |
| `DJANGO_DB_HOST` | Database host | `localhost` or service name |
| `DJANGO_DB_PORT` | Database port | `5432` |

### Optional

| Variable | Description | Default |
|----------|-------------|---------|
| `DJANGO_ALLOWED_HOSTS` | Allowed hosts (comma-separated) | `*` |
| `DJANGO_TIME_ZONE` | Time zone | `UTC` |
| `DJANGO_ADMIN_BASE_URL` | Admin base URL | `http://localhost:8000` |

## Troubleshooting

### Common Issues

1. **Migration conflicts**
   - Ensure all migrations are committed
   - Run `makemigrations --check` locally before pushing

2. **Test failures**
   - Check database connectivity
   - Verify environment variables are set correctly

3. **Deployment failures**
   - Verify all secrets are configured
   - Check deployment platform credentials
   - Review logs for specific errors

4. **Docker build issues**
   - Ensure all dependencies are in requirements.txt
   - Check file permissions
   - Verify PostgreSQL connectivity

## Best Practices

1. **Always test locally** before pushing to CI/CD
2. **Use environment variables** for all sensitive data
3. **Tag releases** with semantic versioning (e.g., v1.0.0)
4. **Enable branch protection** on main/master branch
5. **Review deployment logs** after each deployment
6. **Keep dependencies updated** regularly
7. **Monitor security alerts** from Safety and Bandit

## Next Steps

1. Configure deployment secrets in your CI/CD platform
2. Choose and configure your deployment platform
3. Set up monitoring and logging
4. Configure backup strategies
5. Set up staging environment for testing
6. Implement blue-green or rolling deployments for zero downtime
