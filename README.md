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
4. execute commands inside the container. ex `docker exec -it bingo-backend-app-1 python manage.py makemigrations`

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
DJANGO_SETTINGS_MODULE=config.settings.development
SECRET_KEY=sdfsdfsdf
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_PASSWORD=gmailpassword
EMAIL_HOST_USER=yourmail@gmail.com (gmail_username)
EMAIL_PORT=587
GOOGLE_CLIENT_ID=n.apps.googleusercontent.com
DB_NAME=db_name
DB_USERNAME=db_username
DB_PASSWORD=sdfsdfsdfsdf
DB_HOSTNAME=db_hostname
DB_PORT=5432
DEBUG=True
DJANGO_ALLOWED_HOSTS=tombola.example.it
DJANGO_CORS_ALLOWED_ORIGINS=https://tombola.example.it
DJANGO_CSRF_TRUSTED_ORIGINS=https://tombola.example.it
CADDY_PORT=80
CADDY_EMAIL=example@example.com
DOMAIN=tombola.example.it
```
