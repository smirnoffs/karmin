from rest_framework import routers

from karmin.giftcards.views import GiftCardViewSet

router = routers.DefaultRouter()
router.register('', GiftCardViewSet)

urlpatterns = router.urls
