from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    def get_wallet(self):
        return {
            'usd': self.usd,
            'ton': self.ton,
            'btc': self.btc
        }

