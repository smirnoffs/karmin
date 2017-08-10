import random

from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.views import APIView
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


class GitCardGeneration(APIView):
    http_method_names = ['post', ]

    def post(self, request):
        return self.generate(request)

    def generate(self, request):
        """Generates a new code for a gift cart, recursively repeats the generation if
                    generated code already exists in the database"""
        try:
            number_of_cards = request.data['number_of_cards']
            value = request.data['value']
        except KeyError:
            raise ParseError('Number of cards and value has to be provided')
        generated_codes = []
        for i in range(0, int(number_of_cards)):
            code_exists = True
            while code_exists:
                code = random.randint(10 ** 11, 10 ** 12)
                if not GiftCard.objects.filter(code=code).exists():
                    code_exists = False
            generated_codes.append({'code': code, 'value': value, 'created_by': request.user.pk})
        serializer = GiftCardSerializer(data=generated_codes, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
