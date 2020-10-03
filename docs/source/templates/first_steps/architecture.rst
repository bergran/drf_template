Architecture
============

If you come here from getting started and you were following steps, you will
see the next structure:

| <Project name>
| ├── core
| ├── docs
| ├── hello_world
| ├── main
| ├── .gitignore
| ├── docker-compose.yml
| ├── LICENSE
| ├── manage.py
| ├── README.md
| ├── requirements.in
| └── requirements.txt


Core
----

This directory is a core app module that contains functionalities for extend
models, replace paginator, replace dj-rest-auth for fix a signal that the library
does not send and templates for swagger.

.. note::

    This app module in the future will be placed in a pipy library.

Docs
----

Here, we will save our app docs, you can see an example of how to write them,
his structure and configs.

In other chapter we will make more documentation about this.

hello_world
-----------

An example application for test functionalities.

.. note::
    I personally like to write next structure:

    | <app name>
    | ├── filters /
    | ├── serializers /
    | ├── models /
    | ├── permissions /
    | ├── views /
    | ├── signals /
    | ├── querysets /
    | ├── tests /
    | ├── admin /
    | ├── apps.py
    | └── urls.py


    filters
        Module for save our custom **django_filters.restframework.FilterSet**
    serializers
        Module for save our custom **rest_framework.serializers.Serializer**
    models
        Module for save our **django models**
    permissions
        Module for save our **rest_framework.permissions.BasePermission**
    views
        Module for views

    and so on.


Main
----

This directory is where django save settings, urls and wsgi file. It's created
when you use django-admin and save it with the **project name**, in this template
i configured with this name because i want to sound like main directory of app.

If you want to override this name you has to change in all areas where it's reference
to main directory, in the next files:

* main.settings
* main.wsgi
