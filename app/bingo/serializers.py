from rest_framework import serializers
from .models import Player, Card, Ball, Combination, Winner


class PlayerGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class PlayerPostSerializer(serializers.ModelSerializer):
    player_id = serializers.CharField(source='generate_player_id', read_only=True)

    class Meta:
        model = Player
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    player = PlayerGetSerializer(read_only=True)

    class Meta:
        model = Card
        fields = '__all__'


class BallSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField(read_only=True)
    drawn = serializers.BooleanField(read_only=True)
    drawn_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Ball
        fields = '__all__'


class CombinationSerializer(serializers.ModelSerializer):
    player = PlayerGetSerializer(read_only=True)
    card = CardSerializer(read_only=True)
    ball = BallSerializer(read_only=True)

    class Meta:
        model = Combination
        fields = '__all__'


class WinnerSerializer(serializers.ModelSerializer):
    player = PlayerGetSerializer(read_only=True)
    card = CardSerializer(read_only=True)

    class Meta:
        model = Winner
        fields = '__all__'
