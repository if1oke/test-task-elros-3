from rest_framework import serializers

from wallet.models import USD, TON, BTC


class USDSerializer(serializers.ModelSerializer):
    class Meta:
        model = USD
        fields = ['value']


class TONSerializer(serializers.ModelSerializer):
    class Meta:
        model = TON
        fields = ['address', 'value']


class BTCSerializer(serializers.ModelSerializer):
    class Meta:
        model = BTC
        fields = ['address', 'value']


class WalletInfoSerializer(serializers.Serializer):
    usd = USDSerializer()
    ton = TONSerializer()
    btc = BTCSerializer()
