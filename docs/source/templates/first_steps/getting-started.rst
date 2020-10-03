Getting started
===============

For start with this template you has to:

1. Install django

.. code-block:: bash

    pip install django==<version-project>

In our case we are using django **3.1.2**

2. After install django, we are going to download template with the next command:

.. code-block:: bash

    django-admin startproject --template https://github.com/bergran/drf_template/archive/master.zip <project_name>`

.. note::
    Remember to change **<project_name>** with the name of your project, there are some
    rules that django validate. It should be a slug

    We recommend to execute this command on a **project** directory where you should save
    your all projects

3. Start to develop your own service :D
