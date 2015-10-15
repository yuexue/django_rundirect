# django_rundirect
This is simple Django command to run a custom Python script(or a single line of Python code) with Django settings loaded and environment setup. So you need not put any Django settings related code in your script.

To install this package

    pip install django_rundirect

To integrate this package into a django project, add _'django\_rundirect'_ to Django's INSTALLED_APPS.

Then you can run a python script as:

    python manage.py rundirect SCRIPT.py

You may pass args and options to the custom script, for example:

    python manage.py rundirect SCRIPT.py some_arg --some_option=somevalue

You may run a single line of Python code, for example(like running python -c):

    python manage.py runline "from django.contrib.auth.models import User;print User.objects.count()"

Note that the sys.path will include the path of manage.py(or where you run the python executable).
