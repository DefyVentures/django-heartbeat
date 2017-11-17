
from django.http import HttpResponse
from django.views import generic

from .util import get_checks


def index(request):
    # public | staff | superuser
    logged_in = request.user.is_authenticated()
    if logged_in and request.user.is_superuser:
        return AdminView.as_view()(request)
    elif logged_in and request.user.has_perm('accounts.is_staff'):
        return StaffView.as_view()(request)
    else:
        return PublicView.as_view()(request)


class StatusMixin:
    def get_context_data(self):
        ctx = super().get_context_data()
        result = get_checks(self.request)
        ctx.update({'result': result})
        return ctx


class PublicView(generic.TemplateView):
    template_name = 'heartbeat/public.html'


class StaffView(StatusMixin, generic.TemplateView):
    template_name = 'heartbeat/staff.html'


class AdminView(StatusMixin, generic.TemplateView):
    template_name = 'heartbeat/admin.html'
