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




class Investiments(models.Model):
    one = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    coin = models.ForeignKey(Coin, on_delete=models.SET_NULL, null=True)
    ammount = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.FloatField()
    time = models.DateTimeField(auto_now=True)
    sold = models.BooleanField()

    def __str__(self):
        return '{} - {} - {}'.format(self.one, self.coin, self.price)


    def clean(self):
        owner = Profile.objects.get(self.one)
        coin = Coin.objects.get(self.coin)
        price = self.price
        obj = self.objects.filter(one=owner, coin=coin, price=price)
        if obj.exists():
            raise ValidationError('Investimento ja feito')

    