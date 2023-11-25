from django.db import models
from django_cryptography.fields import encrypt


class CreditCard(models.Model):
    holder = models.CharField("Card Holder", max_length=50)
    number = encrypt(models.CharField("Card Number", max_length=20))
    cvv = models.IntegerField("CVV", blank=True, null=True)
    brand = models.CharField("Card Brand", max_length=20, blank=True, null=True)
    exp_date = models.DateField("Expiration Date")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        try:
            decrypted_last_four = self.number[-4:]
        except Exception as e:
            decrypted_last_four = "****"
        return f"{self.holder}'s Credit Card ending in {decrypted_last_four}"