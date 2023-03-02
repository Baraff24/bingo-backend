import random
from django.utils import timezone
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, filters

from .constants import AMBO, TERNA, QUATERNA, CINQUINA, TOMBOLA, AMBO_WINNERS, TERNA_WINNERS, QUATERNA_WINNERS, \
    CINQUINA_WINNERS, TOMBOLA_WINNERS
from .models import Player, Card, Ball, Combination, Winner
from .serializers import PlayerGetSerializer, PlayerPostSerializer, CardSerializer, BallSerializer, \
    CombinationSerializer, WinnerSerializer
from .utils import generate_card, check_win_n, check_win_tombola


class PlayersListAPI(generics.ListAPIView):
    """
    List all users, with the possibility of filtering by player id, username and numero_matricola.
    Only Admin users can see all the players, while normal users can only see their own data.
    """
    permission_classes = [IsAdminUser]
    serializer_class = PlayerGetSerializer
    queryset = Player.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['player_id', 'username', 'numero_matricola']


class PlayerCreateAPI(APIView):
    """
    Create a new user.
    Only Admin users can create new users.
    """
    permission_classes = [IsAdminUser]
    serializer_class = PlayerPostSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("debug")
            # create a card for the new user
            player = Player.objects.get(player_id=serializer.data['player_id'])
            for i in range(player.numero_di_cartelle):
                Card.objects.create(player=player, card=generate_card())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CardsListAPI(generics.ListAPIView):
    """
    List all cards, with the possibility of filtering by card id, player id and username.
    Only Admin users can see all the cards, while normal users can only see their own cards.
    """
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['card_id', 'player__player_id', 'player__username', 'player__numero_matricola']

    def get_queryset(self):
        queryset = Card.objects.all()
        player_id = self.request.query_params.get('player_id', None)
        if player_id is not None:
            queryset = queryset.filter(player__player_id=player_id)
        return queryset


class BallsListAPI(generics.ListAPIView):
    """
    List of all balls drawn.
    """
    serializer_class = BallSerializer
    queryset = Ball.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['number']

    def get_queryset(self):
        queryset = Ball.objects.all()
        queryset = queryset.filter(drawn=True)
        return queryset 

class BallsDrawAPI(APIView):
    """
    Draw a new ball.
    """
    permission_classes = [IsAdminUser]
    serializer_class = BallSerializer

    def post(self, request):
        # pick a random ball
        balls_objects = list(Ball.objects.filter(drawn=False))
        random_ball = random.choice(balls_objects)

        # set the status of the ball as drawn
        random_ball.drawn = True
        random_ball.drawn_at = timezone.now()
        random_ball.save()

        # check if the new ball is part of any combination
        for card in Card.objects.all():
            for row in card.card:
                for element in row:
                    if element == {'number': str(random_ball.number), 'crossed_out': False}:
                        element['crossed_out'] = True
                        card.save()

            # check if the card has won
            if check_win_n(card.card, 2) and not card.won_ambo:
                Combination.objects.create(player=card.player, card=card, combination=AMBO, won=True,
                                           won_at=timezone.now())
                card.won_ambo = True
                card.save()
                if Winner.objects.filter(type_of_win=AMBO).count() < AMBO_WINNERS:
                    Winner.objects.create(player=card.player, card=card, type_of_win=AMBO, won_at=timezone.now())
                print(f'Player {card.player.username} ha fatto ambo!')
            if check_win_n(card.card, 3) and not card.won_terno:
                Combination.objects.create(player=card.player, card=card, combination=TERNA, won=True,
                                           won_at=timezone.now())
                card.won_terno = True
                card.save()
                if Winner.objects.filter(type_of_win=TERNA).count() < TERNA_WINNERS:
                    Winner.objects.create(player=card.player, card=card, type_of_win=TERNA, won_at=timezone.now())
                print(f'Player {card.player.username} ha fatto terna!')
            if check_win_n(card.card, 4) and not card.won_quaterna:
                Combination.objects.create(player=card.player, card=card, combination=QUATERNA, won=True,
                                           won_at=timezone.now())
                card.won_quaterna = True
                card.save()
                if Winner.objects.filter(type_of_win=QUATERNA).count() < QUATERNA_WINNERS:
                    Winner.objects.create(player=card.player, card=card, type_of_win=QUATERNA, won_at=timezone.now())
                print(f'Player {card.player.username} ha fatto quaterna!')
            if check_win_n(card.card, 5) and not card.won_cinquina:
                Combination.objects.create(player=card.player, card=card, combination=CINQUINA, won=True,
                                           won_at=timezone.now())
                card.won_cinquina = True
                card.save()
                if Winner.objects.filter(type_of_win=CINQUINA).count() < CINQUINA_WINNERS:
                    Winner.objects.create(player=card.player, card=card, type_of_win=CINQUINA, won_at=timezone.now())
                print(f'Player {card.player.username} ha fatto cinquina!')
            if check_win_tombola(card.card) and not card.won_tombola:
                Combination.objects.create(player=card.player, card=card, combination=TOMBOLA, won=True,
                                           won_at=timezone.now())
                card.won_tombola = True
                card.save()
                if Winner.objects.filter(type_of_win=TOMBOLA).count() < TOMBOLA_WINNERS:
                    Winner.objects.create(player=card.player, card=card, type_of_win=TOMBOLA, won_at=timezone.now())
                print(f'Player {card.player.username} ha fatto tombola!')
        serializer = self.serializer_class(random_ball)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CombinationsListAPI(generics.ListAPIView):
    """
    List of all combinations.
    Only Admin users can see all the combinations.
    """
    permission_classes = [IsAdminUser]
    serializer_class = CombinationSerializer
    queryset = Combination.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['combination_id', 'card__card_id', 'card__player__player_id', 'card__player__username',
                     'card__player__numero_matricola', 'ball__ball_id', 'ball__number']


class WinnersListAPI(generics.ListAPIView):
    """
    List of all winners.
    Only Admin users can see all the winners.
    """
    permission_classes = [IsAdminUser]
    serializer_class = WinnerSerializer
    queryset = Winner.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['card__card_id', 'card__player__player_id', 'card__player__username',
                     'card__player__numero_matricola', 'type_of_win']
