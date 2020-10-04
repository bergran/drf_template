Features
========

As we said in the index, this template has some features configured to start play
fast.

In this chapter we will talk about them


Authentication
--------------

Authentication is handled by the library `dj-rest-auth <https://dj-rest-auth.readthedocs.io/en/latest/index.html>`_
library mantained by community that provide minimum endpoints to login in our app
with some providers, in this case is only configured with **JWT** and django users.

It's posible to connect with users from Facebook, Google and so on.

For JWT, we use `djangorestframework-simplejwt <https://django-rest-framework-simplejwt.readthedocs.io/en/latest/>`_,
is a library that provide a lot of configuration for our tokens, also make posible to
disable tokens, this action is posible because tokens are saved in our database.

Also, this library give us 2 endpoints, first for validate and second for refresh.


12 Factor
---------

This template is compliance with this factor.

1. Codebase
2. Dependencies
3. Config
4. Backing services
5. Build, release, run
6. Processes
7. Port binding
8. Concurrency
9. Disposability
10. Dev/prod parity
11. Logs
12. Admin processes

Some of this points are check by django. His codebase is really good,
his dependencies are explicitly, config are managed by diferent files with environment
variable making this the code global for all environments, etc.

For deploy and concurrerncy we used docker and docker-compose. In the app root
is declared a docker compose with redis, postgresql and backend.


Pagination
----------

With django rest framework we have some paginations classes, but in my opinion
i don't like get on response metadata and i customize class for getting this data
on headers, doing more clean response.

Rest Framework

.. code-block::

    {
        "count": 100,
        "next-page: ...,
        "...": ...,
        "results: [{...}}
    }


Customized

.. code-block::

    headers

    Count: 100
    Next-Page: ...
    etc

    body

    [
        {
            "...": ...
        }
    ]


Cors
----

When we develop our apps we dont think about the security we only develop that our
PM tell us, but for our clients is a "must have" so, what is it this feature? and
How it help us? let see it.

CORS (Cross-Origin Resource Sharing) controll what the browser can use with the api
before go to our endpoints checks that the origin of the request is trusted.

How cors knows an origin is trusted? It's simply, we configure it on settings on
**ALLOWED_HOSTS** that it's a list of domains/ip's we trust.

This is not all of CORS, we can tell the client what headers are visible to use.

For this feature we use `Django cors headers <https://github.com/adamchainz/django-cors-headers>`_
that let us a lot of configurations and explanations about this theme.


Settings
--------

Settings has some files for configuration. Thanks to Django we can use a file
for configure what environment we using.

That's why we have:

* **settings.py:** basics settings from django, django rest framework and so on.
* **settings_dev.py:** this file import all settings from **settings.py** and overrides some of these.
* **settings_prod.py:** As we do in settings_dev.py we import from settings but in this case from settings_staging and override some of these for prod. We disable Browserable api, DEBUG and some configurations that only help us for develop phase.
* **settings_staging.py:** configuration for emails, static and database more settings base.

.. note::
    For develop in our local, .gitignore is configured for stage all settings
    describe before, but we can create a new file for example **settings_local.py**
    with configurations that we dont have to upload to our repository.

.. note::
    Remember, we can configure those files with environment variable **DJANGO_SETTINGS_MODULE**


Documentation
-------------

All we know how important is and little time we have to document our app, that's why
this template help you to be easiest document your app.

In API is very important to declare any site where our clients can see what endpoints
have to use, and how they have to use, that's why Swagger/Open api help us to
developers, they make an specification to tell us and show how to we should do.

On debug mode this template is configured for make this action auto.
When we declare our endpoints, we can see it on **http://localhost:8000/api/docs/**
and we will see an interface (Swagger) with endpoints documentation standard,
where we will see method, uri, params and so on. Specification tell us if we want
to add additional comments we can add it on docstrings. More info
`Here <https://www.django-rest-framework.org/topics/documenting-your-api/#a-minimal-example-with-swagger-ui>`_

Also, is very important to document for new developers that are going to start in the
project all the code they see are new and don't know what they are reading, that's
why sphinx is installed. This page or rst that you are reading is done by sphinx.

**Sphinx** is a tool to document very simply with rst files, and docstrings. This
tool can document with docstrings as numpy or google documentation format.

Documentation is saved on **docs/source** directory, with some configurations
and the files. You can see more info `here <https://www.sphinx-doc.org/en/master/>`_

