from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RequestConfig(AppConfig):
    name = 'portxpress.request'
    verbose_name = _("Requests")


    def ready(self):
        try:
            import portxpress.request.signals  # noqa F401
        except ImportError:
            pass
