from django.urls import include, path
from rest_framework import routers

from .views import Events
from .viewsets import ChannelViewset, ChatTypeViewset

router = routers.DefaultRouter()
router.register(r"channels", ChannelViewset, basename="slackchat-channel")
router.register(
    r"chat-types", ChatTypeViewset, basename="slackchat-chat-types"
)

urlpatterns = [
    path("api/", include(router.urls)),
    path("events/", Events.as_view()),
]
