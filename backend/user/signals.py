from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import User
from wallet.models import USD, CryptoAddressBase, TON, BTC


@receiver(post_save, sender=User)
def create_wallets(sender, instance: User, **kwargs):
    if not hasattr(instance, 'usd'):
        setattr(
            instance,
            'usd',
            USD(user=instance).save()
        )
    if not hasattr(instance, 'ton'):
        setattr(
            instance,
            'ton',
            CryptoAddressBase.create(
                TON,
                instance
            )
        )
    if not hasattr(instance, 'btc'):
        setattr(
            instance,
            'btc',
            CryptoAddressBase.create(
                BTC,
                instance
            )
        )