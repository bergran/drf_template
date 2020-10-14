Changelog
=========


0.0.1 (2020-10-04)
------------------

Features
~~~~~~~~
-  **documentation**: add features file. [bergran]

-  **docs**: add master_doc as index instead of default element. [bergran]

-  **docs**: add documentation. [bergran]

-  **project**: add pip-tools for compile requirements and sync. [bergran]

-  **hello_world**: add new app for testing new configurations. [bergran]

-  **project**: upgrade libraries project. [bergran]

  BREAKING CHANGE: django updated to major version 3.1.2, also drf does not allow more TokenProxy
-  **template**: upgrade readme. [bergran]

-  **template**: upgrade requirements. [bergran]

-  **docker**: update python image. [bergran]

-  **docs**: now docs are swagger. [bergran]

-  **requirements**: updated packages. [bergran]

-  **template**: added apps dir to organize apps. [bergran]


Changes
~~~~~~~
-  **requirements**: change django_rest_auth to dj_rest_auth. [bergran]

  django_rest_auth is unmantained and the community make a fork to update the package. Also we changed jwt for the same reason
-  **project**: now all project configs is refactor to main dir. [bergran]


Fix
~~~
-  **settings**: change allowed host to localhost. [bergran]


Other
~~~~~
- Merge pull request #4 from bergran/feature/update-requirements. [Ángel Berhó]

  update dependencies
- Update django version. [bergran]

- Update django to fix security vulnerability. [Ángel Berhó]

- Update django to 2.1.5. [Ángel Berhó]

-  some settings. [Ángel Berhó]

- Update project. [Ángel Berhó]

-  paths. [Ángel Berhó]

- Added kwargs to login_fail signal. [Ángel Berhó]

-  paginator and serializers from project. [Ángel Berhó]

-  function name. [Ángel Berhó]

-  querysets. [Ángel Berhó]

- Refactor function name. [Ángel Berhó]

- Moved to core paginator and serializers. [Ángel Berhó]

- Fix deleteable model behaviour. [Ángel Berhó]

- Removed views from core app. [Ángel]

- Fix readme. [Ángel]

- Fixed import django. [Ángel]

- Added new model behavious and moved to core.models.behaviours. [Ángel]

- Deleted axes and added attempts signals. [Ángel]

- Added models behavious and custom queryset. [Ángel]

  Removed django axes
- Update readme. [Ángel Berhó]

- Added docker-compose file. [Ángel Berhó]

- Fixed some settings. [Ángel Berhó]

- Refactor paginator name. [Ángel Berhó]

- Added another overwrite. [Ángel Berhó]

- Added some utils urls (Login, logout, docs, verify and refresh token) [Ángel Berhó]

- Added django-filters. [Ángel Berhó]

- Gnored static dirs. [Ángel Berhó]

- Added django-axes settings and more docs. [Ángel Berhó]

- Added documentation config and docs. [Ángel Berhó]

- Added documentation to install and config template. [Ángel Berhó]

- Refactor settings staging and prod. [Ángel Berhó]

- Added settings per environment. [Ángel Berhó]

- Configured pagination and login serializer custom. [Ángel]

- Added django-axes. [Ángel]

- Added requirements. [Ángel]

- Ignored venv. [Ángel]

- Add skeleton. [Ángel Berhó]


