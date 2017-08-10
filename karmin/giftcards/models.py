import random

from django.core.exceptions import ValidationError
from django.db import models, IntegrityError


def maximum_10_symbols(value):
    if value > 10 ** 12 - 1:
        raise ValidationError('Код {} довший ніж 12 цифр'.format(value))


CARD_VALUES = (
    (50, '50₴'),
    (100, '100₴'),
    (200, '200₴'),
    (500, '500₴'),
)


class GiftCard(models.Model):
    """
    Model for saving basic information about Gift Cards
    """
    code = models.BigIntegerField(null=False, blank=False, validators=(maximum_10_symbols,), unique=True,
                                  verbose_name="Код")
    value = models.PositiveIntegerField(choices=CARD_VALUES, verbose_name="Вартість")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створений")
    created_by = models.ForeignKey('users.User', verbose_name='Створено', null=False, blank=False)

    class Meta:
        verbose_name = "Подарункова Картка"
        verbose_name_plural = "Подарункові Картки"

    def __str__(self):
        return "Карта {0.code} на {0.value}₴. Створена {0.created_by} {0.created_at:%d.%m.%Y %H:%M}".format(self)

    @classmethod
    def generate_code(cls):
        """Generates a new code for a gift cart, recursively repeats the generation if
        generated code already exists in the database"""
        code_exists = True
        while code_exists:
            code = random.randint(10 ** 11, 10 ** 12)
            if not cls.objects.filter(code=code).exists():
                code_exists = False
        return code

    def save(self, *args, **kwargs):
        if self.sale_set.count():
            raise Exception('Модифікація сертифікатів, що мають продажі не дозволені')
        super(GiftCard, self).save(*args, **kwargs)


class Sale(models.Model):
    card = models.ForeignKey('giftcards.GiftCard')
    sold_by = models.ForeignKey('users.User')
    sold_at = models.DateTimeField(auto_now_add=True)
    used_at = models.DateTimeField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        existing_sale = self.card.sales_set.filter(used_at__isnull=True)
        if self.pk:
            existing_sale = existing_sale.exclude(pk=self.pk)
        if existing_sale.exists():
            raise IntegrityError("This card cannot be resold again, it wasn't cashed")

    class Meta:
        verbose_name = 'Продажа картки'
        verbose_name_plural = 'Продажи карток'
