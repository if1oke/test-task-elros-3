from django.db import models

from core.crypto import create_crypto_addr


class WalletBase(models.Model):
    user = models.OneToOneField(
        'user.User',
        on_delete=models.SET_NULL,
        null=True
    )
    value = models.PositiveIntegerField(
        null=False,
        default=0
    )

    class Meta:
        abstract = True


class CryptoAddressBase(WalletBase):
    address = models.CharField(
        null=False,
        blank=False,
        max_length=64
    )

    @staticmethod
    def create(cls, user):
        return cls(
            user=user,
            address=create_crypto_addr()
        ).save()

    class Meta:
        abstract = True


class USD(WalletBase):
    pass

    class Meta:
        verbose_name = 'USD счет'
        verbose_name_plural = 'USD счета'


class TON(CryptoAddressBase):
    pass

    class Meta:
        verbose_name = 'TON счет'
        verbose_name_plural = 'TON счета'


class BTC(CryptoAddressBase):
    pass

    class Meta:
        verbose_name = 'BTC счет'
        verbose_name_plural = 'BTC счета'
