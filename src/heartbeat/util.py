
from importlib import import_module

from .settings import HEARTBEAT


def get_checks(request):
    """ Return dict with all the checkers data
    """
    result = {}
    for check in HEARTBEAT['checkers']:
        checker_module = import_module(check)
        checker_name = checker_module.__name__.split('.')[-1]
        data = get_check(checker_module, request)
        result.update({checker_name: data})
    return result

def get_check(checker_module, request):
    """ Get checks for checker, pass/fail and data in JSON
    Returns:
        {
            'checks': checks,
            'pass': pass,
            'data': data
        }
    """
    data = checker_module.check(request)
    subchecks = []

    try:
        subchecks = data.get('checks', [])
    except AttributeError:
        pass

    _pass = False not in [c.get('pass') for c in subchecks]
    return {
        'checks': subchecks,
        'pass': _pass,
        'data': data,
    }
