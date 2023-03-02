from django.urls import path

from .views import PlayersListAPI, PlayerCreateAPI, CardsListAPI, BallsListAPI, BallsDrawAPI, CombinationsListAPI, WinnersListAPI

urlpatterns = [
    path('players-list/', PlayersListAPI.as_view(), name='players-list'),
    path('player-create/', PlayerCreateAPI.as_view(), name='player-create'),
    path('cards-list/', CardsListAPI.as_view(), name='cards-list'),
    path('balls-list/', BallsListAPI.as_view(), name='balls-list'),
    path('balls-draw/', BallsDrawAPI.as_view(), name='balls-draw'),
    path('combinations-list/', CombinationsListAPI.as_view(), name='combinations-list'),
    path('winners-list/', WinnersListAPI.as_view(), name='winners-list'),
]
