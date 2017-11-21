from django.conf import settings


def debug_mode(request):
    return settings.DEBUG
