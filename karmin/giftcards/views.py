from rest_framework.viewsets import ModelViewSet

from karmin.giftcards.models import GiftCard
from karmin.giftcards.serializers import GiftCardSerializer


class GiftCardViewSet(ModelViewSet):
    queryset = GiftCard.objects.all()
    serializer_class = GiftCardSerializer
