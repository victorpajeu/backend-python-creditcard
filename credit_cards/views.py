from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# models
from credit_cards.models import CreditCard

# serializer
from credit_cards.serializers import CreditCardSerializer


class CreditCardViewSet(ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    permission_classes = [IsAuthenticated]
