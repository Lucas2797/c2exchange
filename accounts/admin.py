from django.contrib import admin
from . models import Investiments, Profile



class ProfileConfig(admin.ModelAdmin):
    list_display = ('user', 'created_at')


class InvestimentsConfig(admin.ModelAdmin):
    list_display = ('one', 'coin', 'ammount', 'price', 'time', 'sold')



admin.site.register(Profile, ProfileConfig),
admin.site.register(Investiments, InvestimentsConfig),
