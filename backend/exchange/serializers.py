from rest_framework import serializers

from exchange.models import Rates


class RateSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['ton'] = round(float(data['ton'] / 100), 2)
        data['btc'] = round(float(data['btc'] / 100), 2)
        return data

    class Meta:
        model = Rates
        fields = ['ton', 'btc']
