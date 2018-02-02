from django.views import generic

from heartbeat.util import get_status


class StatusView(generic.TemplateView):
    template_name = 'heartbeat/status.html'

    def get_context_data(self):
        context = super().get_context_data()
        status = get_status(self.request)
        context.update(status)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        status = 200
        if context['status']['pass'] is not True:
            status = 500
        return self.render_to_response(context, status=status)
