# Django template

## Technologies

- [X] Python
- [X] Django
- [X] Django Rest Framework
- [X] Docker
- [X] Postgresql
- [X] Ruff

## Environments

This template is thought and designed for the docker environment. It is not recommended to use it without docker.


### How to use Docker dev

1. create a file named `.env` containing the required environment variables (read the next section)
2. run `docker compose up --build` for dev or `docker compose -f docker-compose.prod.yml up --build` for prod
3. work with your local files
4. execute commands inside the container. ex `docker exec -it shape-hunters-backend-app-1 python manage.py makemigrations`

Use Ruff to check the code quality. `ruff` command is already installed inside the container.
Example: `docker exec -it django-template-app-1 ruff check .` 

### Features

| Features                           |                            |
|------------------------------------|:--------------------------:|
| Auto-reload                        |            ❌ No            |
| Auto migrate at start              |             ✅              |
| Auto requirements install at start |             ✅              |
| Database                           |          MariaDB           |
| Database port publicly exposed     |             ✅              |
| Reverse proxy (Nginx)              |        ⚠️ Optional         |
| Debug                              | ⚠️ Optional (default=True) |
| Admin page                         |             ✅              |
| Serving media automatically        |             ✅              |
| CORS allow all                     |  ❌ No (default=localhost)  |
| Allow all hosts                    |  ❌ No (default=localhost)  |

There is google oauth2 authentication already implemented with django-allauth.
You have to create a google oauth2 app and add the credentials to the admin page.


### Required environment variables

- ✅ Required
- ❌ Not required
- ⚠️ Optional

| Variables                   |    |
|-----------------------------|:--:|
| DJANGO_SETTINGS_MODULE      | ✅  |
| DB_NAME                     | ✅  |
| DB_USERNAME                 | ✅  |
| DB_PASSWORD                 | ✅  |
| DB_HOSTNAME                 | ✅  |
| DB_PORT                     | ✅  |
| SECRET_KEY                  | ⚠️ |
| EMAIL_HOST                  | ⚠️ |
| EMAIL_HOST_PASSWORD         | ⚠️ |
| EMAIL_HOST_USER             | ⚠️ |
| EMAIL_PORT                  | ⚠️ |
| DEBUG                       | ⚠️ |
| DJANGO_ALLOWED_HOSTS        | ✅  |
| DJANGO_CORS_ALLOWED_ORIGINS | ✅  |
| DJANGO_CSRF_TRUSTED_ORIGINS | ✅  |
| NGINX_PORT                  | ✅  |

### Example .env

```
DJANGO_SETTINGS_MODULE=core.config.settings.development (or .production)
SECRET_KEY=anotherrandomstring
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_PASSWORD=gmailpassword (Turn ON two factor authentication of gmail account, and create an app password - https://support.google.com/accounts/answer/185833)
EMAIL_HOST_USER=yourmail@gmail.com (gmail_username)
EMAIL_PORT=587
DB_NAME=somerandomname
DB_USERNAME=somerandomusername
DB_PASSWORD=somerandomstring
DB_HOSTNAME=database
DB_PORT=5432
DEBUG=True
DJANGO_ALLOWED_HOSTS=*
DJANGO_CORS_ALLOWED_ORIGINS=http://localhost:5000
DJANGO_CSRF_TRUSTED_ORIGINS=http://localhost:5000
NGINX_PORT=80
```


### Certbot

If command `docker-compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ --dry-run -d [domain-name]` run correctly, run it without `--dry-run` flag to make it.

To renew the certificate, run `docker-compose run --rm certbot renew`