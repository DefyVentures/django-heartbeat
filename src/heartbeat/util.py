
import json

from django.utils.module_loading import import_string

from .settings import HEARTBEAT


def get_checks(request):
    """ Return dict with all the checkers data
    """
    result = {}
    for check in HEARTBEAT['checkers']:
        check_fn = import_string(check)
        checker_name = check_fn.__name__.split('.')[-1]
        checker_name = checker_name.replace('_', ' ')  # replace underscore
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
        'data': json.dumps(data, indent=2),
    }

def get_status(request):
    result = get_checks(request)

    # check that everything is passing
    checks_passed = 0
    for check, check_dict in result.items():
        if check_dict['pass'] == True:
            checks_passed += 1
    lcms_pass = True if checks_passed == len(result) else False
    lcms_status = {
        'label': 'The LCMS is up and running.',
        'pass': lcms_pass
    }

    return {
        'result': result,
        'status': lcms_status,
    }
