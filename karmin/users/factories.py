from factory import DjangoModelFactory, Faker

from karmin.users.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Faker('user_name')
    email = Faker('email')
