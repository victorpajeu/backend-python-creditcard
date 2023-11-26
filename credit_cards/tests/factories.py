from factory.django import DjangoModelFactory
from credit_cards.models import CreditCard


class CreditCardFactory(DjangoModelFactory):
    holder = "Holder name"
    number = "123456789101112"
    cvv = 123
    brand = "Visa"
    exp_date = "2032-01-02"

    class Meta:
        model=CreditCard
        abstract = False
