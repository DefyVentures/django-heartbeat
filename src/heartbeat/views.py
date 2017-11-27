
from django.http import HttpResponse
from django.views import generic

from .util import get_checks


class StatusView(generic.TemplateView):
    template_name = 'heartbeat/status.html'

    def get_context_data(self):
        ctx = super().get_context_data()
        result = get_checks(self.request)

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

        base_template = 'base.html'
        if self.request.user.is_authenticated():
            base_template = 'dashboard.html'

        ctx.update({
            'result': result,
            'status': lcms_status,
            'base_template': base_template
        })
        return ctx
