from factory import DjangoModelFactory, Faker
from factory.declarations import SubFactory
from factory.fuzzy import FuzzyChoice

from karmin.giftcards.models import GiftCard, CARD_VALUES


class GiftCardFactory(DjangoModelFactory):
    class Meta:
        model = GiftCard

    code = Faker('random_int', min=10 ** 11, max=10 ** 12)
    created_at = Faker('date_time_this_decade')
    created_by = SubFactory('karmin.users.factories.UserFactory')
    value = FuzzyChoice(value[0] for value in CARD_VALUES)
