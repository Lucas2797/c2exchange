from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import get_user_model
from coins.models import Coin

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{}'.format(self.user.username)


class Wallet(models.Model):
    one = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="wallet")



class Investiment(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.SET_NULL, null=True, related_name="invest")
    coin = models.ForeignKey(Coin, on_delete=models.SET_NULL, null=True, related_name="invest")
    ammount = models.FloatField()
    payd = models.FloatField()
    time = models.DateTimeField(auto_now=True)
    sold = models.BooleanField(default=False)
    # last_profit = models.FloatField()

    def __str__(self):
        return '{} - {} - {}'.format(self.one, self.coin, self.payd)

    @property
    def profit(self):
        ''' Defining property profit better than a field. In order to update without Patch '''
        return (self.coin.price * self.ammount) - (self.payd * self.ammount)

    @property
    def profit_percent(self):
        ''' Defining property profit better than a field. In order to update without Patch '''
        return (self.coin.price * 100)/self.payd  - 100
    


    def clean(self):
        owner = Profile.objects.get(id=self.one.id)
        coin = Coin.objects.get(id=self.coin.id)
        payd = self.payd
        time = self.time
        obj = Investiment.objects.filter(one=owner, coin=coin, payd=payd)
        if obj.exists():
            raise ValidationError('Investimento ja feito')

    