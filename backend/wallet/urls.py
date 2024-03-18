from django.urls import path
from wallet.views import WalletInfoView

urlpatterns = [
    path('', WalletInfoView.as_view(), name='user-wallet')
]
