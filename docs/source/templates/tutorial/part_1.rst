Tutorial part 1
###############

After read a lot of documentation about this template, you got it, now
go to practise how to make an API fast.

First of all we need to define a context to create our API, in this tutorial
we will make a poll app, like `Django tutorial <https://docs.djangoproject.com/en/3.1/intro/tutorial01/>`_


Create django project and app
-----------------------------

we will create our project. let's call it **Poll app**.

.. code-block::

    $ django-admin startproject --template https://github.com/bergran/drf_template/archive/master.zip poll_app

.. note::

    Remember we need to install django before execute the command, you can see
    this on :doc:`../first_steps/getting-started`.


After create our project, let's create our **poll app**, where we will develop
our poll logic.

.. code-block::

    $ python manage.py startapp poll

After execute this command, a new directory will appear on our project called
poll as we execute in the command. Nice! now we will install this app in the
project. For this task, we need to modify on **main/settings/settings.py** file
the **PROJECT_APPS** variable, adding the new app as new item

.. code-block::

    PROJECT_APPS = [
        ...
        'poll',
    ]

After modify this variable, all models from this app will watch for new
changes and will create and apply migrations.


Create Models
-------------

Let's start to develop our model logic, for our poll app we need a Polls and
Answers models. We will add it into **models.py** file

.. code-block::

    from django.db import models
    from core.models.behaviours import Timestampable


    class Question(Timestampable, models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')


    class Choice(Timestampable, models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)


We can see we created two classes that inherits from Timestampable and
models.Model. **Timestampable** add two fields, **created** and **modified**
as his name tell us, created is a datetime that will be apply by default on
instance created and modified after create or modify actions. **models.Model**
tell this class is a Django Model and then it will watch for new changes.

For create migrations we need to execute next code

.. code-block::

    $ python manage.py makemigrations


Django now see we have 2 new models, **Question** and **Choice** and to apply
this migration to our database we need to execute next command:

.. code-block::

    $ python manage.py migrate

After execute this command, django raise an error, this error is we didn't
configure any database, so our configuration does not exist.

We will see later in the deploy section, don't worry. We will fix this error
executing next line

.. code-block::

    docker run --name poll-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
