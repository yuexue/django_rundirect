'''
A Django command to run Python scripts directly.
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
    index = sys.argv.index('rundirect')
    after = []
    length = len(sys.argv)
    for i in range(index + 1, length):
        after.append(sys.argv.pop(index + 1))
    return sys.argv, after


class Command(BaseCommand):
    help = '''Run a script with django settings directly:

python manage.py rundirect SCRIPT.py [args] [options]

args and options are for the SCRIPT.py.
'''

    def __init__(self, *args, **options):
        BaseCommand.__init__(self, *args, **options)

    def handle(self, *args, **options):
        filename = self.after[0]
        exec_globals = globals()
        exec_globals['__name__'] = '__main__'
        execfile(filename, exec_globals)

# Hack the sys.argv, make sure BaseComamnd.run_from_argv
# doesn't get any undeclared options.
Command.before, Command.after = split_argv()
