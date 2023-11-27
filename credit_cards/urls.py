from rest_framework import routers
from credit_cards.views import CreditCardViewSet


router = routers.DefaultRouter()
router.register(r'credit-card', CreditCardViewSet)