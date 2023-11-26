from rest_framework import serializers

# Models
from creditcard import CreditCard

class CreditCardSerializer(serializers.ModelSerializer):
    holder = serializers.CharField(min_length=3)
    number = serializers.CharField()
    cvv = serializers.IntegerField(min_value=100, max_value=9999)
    brand = serializers.CharField(read_only=True)
    exp_date = serializers.DateField(format='%m/%Y', input_formats=['%m/%Y'])

    class Meta:
        model = CreditCard
        fields = ('holder', 'number', 'cvv', 'brand', 'exp_date')