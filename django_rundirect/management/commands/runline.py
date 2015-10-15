'''
A Django command to run a single line of Python code.
'''
import sys
from django.core.management.base import BaseCommand


def split_argv():
    '''
    Split the sys.argv into two halves,
    Django will use the first half,
    the second half will be pass to the user
    defined script.
    '''
    index = sys.argv.index('runline')
    after = []
    length = len(sys.argv)
    for i in range(index + 1, length):
        after.append(sys.argv.pop(index + 1))
    return sys.argv, after


class Command(BaseCommand):
    help = '''Run a single line of Python code with django settings directly:

    python manage.py runline "<Your Commandline>"

Example:

    python manage.py runline "from django.contrib.auth.models import User;print User.objects.count()"
'''

    def __init__(self, *args, **options):
        BaseCommand.__init__(self, *args, **options)

    def handle(self, *args, **options):
        line = ' ' if not self.after else self.after[0]
        print repr(line)
        exec(line)

# Hack the sys.argv, make sure BaseComamnd.run_from_argv
# doesn't get any undeclared options.
Command.before, Command.after = split_argv()
