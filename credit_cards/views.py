from rest_framework.viewsets import ModelViewSet

# models
from credit_cards.models import CreditCard

# serializer
from credit_cards.serializers import CreditCardSerializer


class CreditCardViewSet(ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
