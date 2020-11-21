from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from portxpress.users.api.views import UserViewSet, AgentViewSet, TransporterViewSet
from portxpress.news.api.views import NewsViewSet, TrafficViewSet
from portxpress.request.api.views import RequestViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("agents", AgentViewSet)
router.register("transporters", TransporterViewSet)
router.register("news", NewsViewSet)
router.register("traffics", TrafficViewSet)
router.register("requests", RequestViewSet)

app_name = "api"
urlpatterns = router.urls
