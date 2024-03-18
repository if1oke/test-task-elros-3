from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from exchange.models import Rates
from exchange.serializers import RateSerializer


class CurrentRatesView(GenericAPIView):
    serializer_class = RateSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = self.get_serializer(Rates.get_current_rate())
        return Response(serializer.data)


class Last5RatesView(CurrentRatesView):
    def get(self, request):
        serializer = self.get_serializer(Rates.get_last_5_rates(), many=True)
        return Response(serializer.data)
