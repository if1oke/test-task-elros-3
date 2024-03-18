from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from wallet.serializers import WalletInfoSerializer


class WalletInfoView(GenericAPIView):
    serializer_class = WalletInfoSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        serializer = self.get_serializer(self.request.user.get_wallet())
        return Response(serializer.data)
