
from django.utils.module_loading import import_string

from .settings import HEARTBEAT


def get_checks(request):
    """ Return dict with all the checkers data
    """
    result = {}
    for check in HEARTBEAT['checkers']:
        check_fn = import_string(check)
        checker_name = check_fn.__name__.split('.')[-1]
        data = get_check(check_fn, request)
        result.update({checker_name: data})
    return result

def get_check(check_fn, request):
    """ Get checks for checker, pass/fail and data in JSON
    Returns:
        {
            'checks': checks,
            'pass': pass,
            'data': data
        }
    """

    data = check_fn(request)
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
