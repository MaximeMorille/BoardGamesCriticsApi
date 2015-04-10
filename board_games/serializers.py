from rest_framework import serializers

from board_games.models import BoardGame


class BoardGameSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = BoardGame
        fields = ('id', 'name', 'owner', 'editor')
