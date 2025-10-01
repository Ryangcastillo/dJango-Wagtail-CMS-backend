# Security Policy

## Supported Versions

We release patches for security vulnerabilities in the following versions:

| Version | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability, please follow these steps:

1. **Do NOT** open a public issue
2. Email the maintainers directly at [security email - update this]
3. Include the following information:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if available)

## What to Expect

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Fix Timeline**: Depends on severity
  - Critical: Within 24-48 hours
  - High: Within 1 week
  - Medium: Within 2 weeks
  - Low: Within 1 month

## Security Best Practices

### For Deployment

1. **Always use HTTPS** in production
2. **Set strong SECRET_KEY**: Generate a unique, random key
3. **Disable DEBUG** in production (`DJANGO_DEBUG=0`)
4. **Set ALLOWED_HOSTS** to your domain(s)
5. **Use environment variables** for all secrets
6. **Keep dependencies updated**: Run `pip list --outdated` regularly
7. **Enable CSRF protection** (enabled by default)
8. **Use secure session cookies**: Set `SESSION_COOKIE_SECURE=True`
9. **Use secure CSRF cookies**: Set `CSRF_COOKIE_SECURE=True`
10. **Set security headers**: Use Django's security middleware

### Database Security

1. Use strong database passwords
2. Restrict database access by IP
3. Use SSL/TLS for database connections
4. Regular backups with encryption

### CI/CD Security

1. Store secrets in GitHub/GitLab Secrets, not in code
2. Use read-only tokens where possible
3. Enable branch protection on main
4. Require reviews before merging
5. Run security scans in CI pipeline

## Security Features

This project includes:

- ✅ Django's built-in security middleware
- ✅ CSRF protection
- ✅ SQL injection protection (via ORM)
- ✅ XSS protection (via template auto-escaping)
- ✅ Clickjacking protection
- ✅ SSL/HTTPS redirects (production)
- ✅ Security checks in CI/CD pipeline
- ✅ Dependency vulnerability scanning (Safety)
- ✅ Security linting (Bandit)

## Security Checklist for Deployment

Before deploying to production:

- [ ] `DJANGO_SECRET_KEY` is unique and secure
- [ ] `DJANGO_DEBUG=0`
- [ ] `ALLOWED_HOSTS` is properly configured
- [ ] All secrets are in environment variables
- [ ] Database credentials are strong
- [ ] HTTPS is enabled
- [ ] Security middleware is enabled
- [ ] `python manage.py check --deploy` passes
- [ ] All dependencies are up to date
- [ ] Security scans pass
- [ ] Backups are configured

## Known Security Considerations

- Wagtail admin is accessible at `/cms/` - protect with strong passwords
- Django admin is accessible at `/django-admin/` - protect with strong passwords
- API endpoints at `/api/v2/` - configure appropriate permissions
- Ensure integration credentials are encrypted at rest

## Updates and Patches

Security patches will be released as soon as possible after a vulnerability is confirmed. Users should:

1. Subscribe to repository notifications
2. Monitor security advisories
3. Apply security updates promptly
4. Test updates in staging before production

## Additional Resources

- [Django Security Documentation](https://docs.djangoproject.com/en/stable/topics/security/)
- [Wagtail Security](https://docs.wagtail.org/en/stable/advanced_topics/deploying.html#security)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)

Thank you for helping keep Debuttend CMS secure!
