
from django.http import HttpResponse
from django.views import generic

from heartbeat.util import get_status


class StatusView(generic.TemplateView):
    template_name = 'heartbeat/status.html'

    def get_context_data(self):
        ctx = super().get_context_data()
        status = get_status(self.request)
        ctx.update(status)
        return ctx
