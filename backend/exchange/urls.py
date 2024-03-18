from django.urls import path

from exchange.views import CurrentRatesView, Last5RatesView

urlpatterns = [
    path('rate/', CurrentRatesView.as_view(), name='exchange-rate'),
    path('rate/history/', Last5RatesView.as_view(), name='exchange-rate-history'),
]