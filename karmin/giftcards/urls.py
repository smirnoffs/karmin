from django.conf.urls import url
from rest_framework import routers

from karmin.giftcards.views import GiftCardViewSet, GitCardGeneration

urlpatterns = [
    url(r'^generate/$', GitCardGeneration.as_view())
]

router = routers.DefaultRouter()
router.register('', GiftCardViewSet)

urlpatterns += router.urls
