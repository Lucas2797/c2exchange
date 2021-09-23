from django.contrib import admin
from . models import Investiment, Profile, Wallet



class ProfileConfig(admin.ModelAdmin):
    list_display = ('user', 'created_at')

class WalletConfig(admin.ModelAdmin):
    list_display = ('one',)

class InvestimentConfig(admin.ModelAdmin):
    list_display = ('wallet', 'coin', 'ammount', 'payd', 'time', 'sold')



admin.site.register(Profile, ProfileConfig),
admin.site.register(Investiment, InvestimentConfig),
admin.site.register(Wallet, WalletConfig),
