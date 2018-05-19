# Drf template

This is a template for django rest framework

The goal is to start a django application fast
with a lot of configuration and does not wate time
on configure it

## Requirements

* Python 3 or higher
* Docker 17 or higher
* Docker-compose
* Nginx

## Install template

To install this template you only need to have
django 2 or higher installed. Then,
execute
`python3 manage.py startproject --template https://github.com/bergran/drf_template/archive/master.zip`.
This command will create a django project with the configuration
to create api rest faster.

## Authentication

This template has mount some methods to authenticate that can be
different per environment.

* Jwt token: Global in all environments
* Session (Cookie): Only development and staging environment has this permission
* Basic authentication: Only development and staging environment has this permission

Authentication is protected by django axes with a maximum number of 3 failed attempts per minute.

## Pagination

This template is configured to paginate responses
with the next headers:
* Next-Page: Next page number. If not next then will be `null`
* Previous-Page: Previous page number. If not previous then will be `null`
* Last-Page: Last page number. 
* Count: Elements total number.

You can configure elements number per page with `PAGE_SIZE`.

## Api documentation

Documentation it's gonna be automatic. When you add endpoints to
router from rest framework this will add too to here.

You can interact with this documentation. This means you can
request your endpoints from the web that coreapi provides.

It's published on `/api/docs/` and only can be access if the user is logged with
django Session (cookie)

Documentation is from coreapi library. You can see more info
[here](http://www.django-rest-framework.org/topics/documenting-your-api/)

## Configuration global(Environment variables)

* DJANGO_SETTINGS_MODULE: Config environment configuration, you can see more
info on `Environments` section. Default: `project.settings`
* SECRET_KEY: Secret key. This is used on hash password and jwt.
default `'y-=ta...`
* ALLOWED_HOST: Allowed host origin, others will be fail. Default `127.0.0.1`
* PAGE_SIZE: Elements number per page on list endpoints. Default `20`
* REFRESH_EXPIRATION_MINUTES: Time in minutes to expirate refresh jwt token.
default `15 minutes`
* TOKEN_EXPIRATION_MINUTES: Time since the token was created or refreshed to not allow more tokens.
Default `1440 minutes (1 day)`
* TOKEN_PREFIX: Prefix on JWT `Authentication` header. Default `Bearer`
* REDIS_CACHE_LOCATION: Path to redis. Default `redis://127.0.0.1:6379/1`
* POSTGRES_DB: DB Name postgres database. Default `myproject`
* POSTGRES_USER: DB User postgres. Default `myproject`
* POSTGRES_PASSWORD: DB Password postgres. Default `myproject`
* POSTGRES_HOST: DB Host postgres. Default `127.0.0.1`
* POSTGRES_PORT: DB Port postgres. Default `5432`

## Configuration Staging/production(Environment variables)

* STATIC_URL: Static url files. Default `/static/`
* STATIC_ROOT: Static storage files. Default `static`
* MEDIA_URL: Media url files. Default `/media/`
* MEDIA_ROOT: Media storage files. Default `media`
* DEFAULT_FROM_EMAIL: From email when a email will send. Default ``
* EMAIL_HOST: Host smtp path. Default ``
* EMAIL_PORT: Port smtp path. Default ``
* EMAIL_HOST_USER: User credential server smtp. Default ``
* EMAIL_HOST_PASSWORD: Password credential server smtp. Default ``

example `.env` file:
```
    DJANGO_SETTINGS_MODULE=project.settings
    SECRET_KEY=x8R]j(4epfVD`3Xc
    ALLOWED_HOST=127.0.0.1
    PAGE_SIZE=20
    REFRESH_EXPIRATION_MINUTES=25
    TOKEN_EXPIRATION_MINUTES=60
    TOKEN_PREFIX=Bearer
    REDIS_CACHE_LOCATION=redis://127.0.0.1:6379/1
    POSTGRES_DB=myproject
    POSTGRES_USER=myproject
    POSTGRES_PASSWORD=myproject
    POSTGRES_HOST=myproject
    POSTGRES_PORT=myproject
    STATIC_URL=\/static\/
    STATIC_ROOT=static
    MEDIA_URL=\/media\/
    MEDIA_ROOT=media
    DEFAULT_FROM_EMAIL=pepito@patatita123.com
    EMAIL_HOST=127.0.0.1
    EMAIL_PORT=25
    EMAIL_HOST_USER=pepito@patatita123.com
    EMAIL_HOST_PASSWORD=SuperSecurePassword
```

## Environments

1. Development
    
    To start with development environment you has to
    set environment variable `DJANGO_SETTINGS_MODULE` to
    `project.settings_dev`
    
    Development environment configuration let you
    to program with coreapi/browseable documentation
    that you can interact with
    the endpoints and see documentation about them.
    Also, it's configured to default format on django test
    client send data as application/json.
    This environment is usually used to develop backend.

2. Staging

    To start with staging environment you has to
    set environment variable `DJANGO_SETTINGS_MODULE` to
    `project.settings_staging`
    
    Staging environment configuration is very similar to development environment
    but this environment has more configuration as static and media urls or
    email configuration. This environment is usually used to develop a client.

3. Production

    To start with production environment you has to
    set environment variable `DJANGO_SETTINGS_MODULE` to
    `project.settings_prod`
    
    Production environment configuration has all staging configuration except
    debug is set to false, that means django wont show errors on endpoint responses.
    Also, it wont serve browseable api and the coreapi will be disabled.
    Authentication only active will be JsonWebTokens on `Authentication` header

## Deploy

Most likely in docker but Work in progress...

## Author

Ángel Berhó Grande