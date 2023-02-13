from django.urls import include, path
from rest_framework import routers

from .views import Events, ChannelDeserializer
from .viewsets import ChannelViewset, ChatTypeViewset

router = routers.DefaultRouter()
router.register(r"channels", ChannelViewset, basename="slackchat-channel")
router.register(
    r"chat-types", ChatTypeViewset, basename="slackchat-chat-types"
)

urlpatterns = [
    path("api/read/", include(router.urls), name="api-read"),
    path("api/write/", ChannelDeserializer.as_view(), name="api-write"),
    path("events/", Events.as_view(), name="api-events"),
]
