from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from karmin.giftcards.models import GiftCard
from karmin.giftcards.serializers import GiftCardSerializer


class GiftCardViewSet(ModelViewSet):
    queryset = GiftCard.objects.all()
    serializer_class = GiftCardSerializer

    def create(self, request, *args, **kwargs):
        many = False
        request_data = request.data
        if isinstance(request.data, list):
            many = True
        serializer = self.get_serializer(data=request_data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
