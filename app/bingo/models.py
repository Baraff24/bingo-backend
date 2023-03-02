import random
from django.db import models
from django.contrib.postgres.fields import ArrayField

from .constants import COMBINATIONS_CHOICES, NOTHING


class Player(models.Model):
    player_id = models.CharField(unique=True, max_length=6)
    username = models.CharField(max_length=255)
    numero_matricola = models.CharField(max_length=6, unique=True, null=True, blank=True)
    numero_di_cartelle = models.IntegerField(default=1)

    def __str__(self):
        return "player id: {} - username: {} - numero matricola: {} - numero di cartelle: {}".format(self.player_id,
                                                                                                     self.username,
                                                                                                     self.numero_matricola,
                                                                                                     self.numero_di_cartelle)

    def generate_player_id(self):
        """
        Generate a random unique user id.
        """
        random_player_id = str(random.randint(100000, 999999))
        if Player.objects.filter(player_id=random_player_id).exists():
            return self.generate_player_id()
        else:
            self.player_id = random_player_id
            self.save()
            return self.player_id

    class Meta:
        verbose_name = 'player'
        verbose_name_plural = 'players'
        ordering = ['id']


class Card(models.Model):
    card_id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    won_ambo = models.BooleanField(default=False)
    won_terno = models.BooleanField(default=False)
    won_quaterna = models.BooleanField(default=False)
    won_cinquina = models.BooleanField(default=False)
    won_tombola = models.BooleanField(default=False)
    card = ArrayField(
        ArrayField(
            models.JSONField(),
            size=9,
        ),
        size=3,
        serialize=True,
    )

    def __str__(self):
        return "card id: {} - user: {}".format(self.card_id, self.player)

    class Meta:
        verbose_name = 'card'
        verbose_name_plural = 'cards'
        ordering = ['card_id']


class Ball(models.Model):
    number = models.IntegerField()
    drawn = models.BooleanField(default=False)
    drawn_at = models.DateTimeField(null=True)

    def __str__(self):
        return "number: {} - drawn: {} - drawn at: {}".format(self.number, self.drawn, self.drawn_at)

    class Meta:
        verbose_name = 'ball'
        verbose_name_plural = 'balls'


class Combination(models.Model):
    combination = models.CharField(max_length=255, choices=COMBINATIONS_CHOICES, default=NOTHING)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    won = models.BooleanField(default=False)
    won_at = models.DateTimeField(null=True)

    def __str__(self):
        return "combination: {} - player: {} - card: {} - won: {} - won at: {}".format(self.combination,
                                                                                       self.player,
                                                                                       self.card,
                                                                                       self.won,
                                                                                       self.won_at)

    class Meta:
        verbose_name = 'combination'
        verbose_name_plural = 'combinations'
        ordering = ['combination']


class Winner(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    type_of_win = models.CharField(max_length=255, choices=COMBINATIONS_CHOICES, default=NOTHING)
    won_at = models.DateTimeField(null=True)

    def __str__(self):
        return "player: {} - card: {} - won at: {}".format(self.player, self.card, self.won_at)

    class Meta:
        verbose_name = 'winner'
        verbose_name_plural = 'winners'
        ordering = ['type_of_win', 'won_at']
