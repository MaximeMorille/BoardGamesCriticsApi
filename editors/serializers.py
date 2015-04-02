from rest_framework import serializers

from editors.models import Editor


class EditorSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Editor
        fields = ('id', 'name', 'owner')

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    editors = serializers.PrimaryKeyRelatedField(many=True,
                                                 queryset=Editor.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'editors')
