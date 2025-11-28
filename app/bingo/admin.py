from django.contrib import admin
from .models import (Player, Card, Ball,
                     Combination, Winner, AvailableCombination)

admin.site.register(Player)
admin.site.register(Card)
admin.site.register(Ball)
admin.site.register(Combination)
admin.site.register(Winner)
admin.site.register(AvailableCombination)
