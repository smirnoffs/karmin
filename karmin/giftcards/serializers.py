from rest_framework.serializers import ModelSerializer

from karmin.giftcards.models import GiftCard


class GiftCardSerializer(ModelSerializer):
    class Meta:
        model = GiftCard
        fields = '__all__'
