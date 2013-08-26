# django_rundirect
This is simple Django command to run a custom script with Django settings.

To integrate this package into a django project, add _'django\_rundirect'_ to Django's INSTALLED_APPS.

Then you can run a python script as:

    python manage.py rundirect SCRIPT.py

You may pass args and options to the custom script, for example:

    python manage.py rundirect SCRIPT.py some_arg --some_option=somevalue

Note that the sys.path will include the path of manage.py(or where you run the python executable).
