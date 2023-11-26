from django.test import TestCase
from credit_cards.tests.factories import CreditCardFactory


class CreditCardModelTest(TestCase):
    def test_unicode_str(self):
        credit_card = CreditCardFactory()
        self.assertEqual(str(credit_card), f"{credit_card.holder}'s Credit Card ending in {credit_card.number[-4:]}")
