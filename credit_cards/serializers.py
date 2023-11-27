import calendar
from datetime import datetime
from rest_framework import serializers


# Models
from creditcard import CreditCard

class CreditCardSerializer(serializers.Serializer):
    holder = serializers.CharField(min_length=3)
    number = serializers.CharField()
    cvv = serializers.IntegerField(min_value=100, max_value=9999)
    brand = serializers.CharField(read_only=True)
    exp_date = serializers.DateField(format='%m/%Y', input_formats=['%m/%Y'])

    def create(self, data):
        cc = CreditCard(data.get('number'))
        if cc.is_valid():
            data['brand'] = cc.get_brand()
            exp_date = data['exp_date']
            if exp_date > datetime.today().date():
                data['exp_date'] = exp_date.replace(day=calendar.monthrange(exp_date.year, exp_date.month)[1])
                return CreditCard.objects.create(**data)
            raise serializers.ValidationError("Invalid date")
        raise serializers.ValidationError("Card number provided is invalid")