==============
cuac developer
==============

It is the developer package for Django Cuac.

Quick start
-----------


1. Add "cuac_developer" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "cuac_developer",
    ]

2. Include the polls URLconf in your project urls.py like this::

    path("core/", include("cuac_developer.urls")),

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).