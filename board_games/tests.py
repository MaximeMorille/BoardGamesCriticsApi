# -*- coding: utf8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.

from board_games.models import BoardGame
from editors.models import Editor
from django.contrib.auth.models import User


class BoardGameMethodTests(TestCase):

    def test_unicode(self):
        """
        __unicode__() should returns the name of the editor
        """
        boardGame = BoardGame(name='Bang! Le jeu de dés')
        boardGame.save()
        self.assertEqual(boardGame.__unicode__(), 'Bang! Le jeu de dés')


class BoardGameViewTests(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.user = User.objects.create_user(
            username='test',
            email='test@mail.com',
            password='testing'
        )

        self.editor = Editor.objects.create(
            name='Asmodée',
            owner=self.user
        )

    def test_index(self):
        response = self.client.get(reverse('boardgame-list'))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.post(
            reverse('boardgame-list'),
            {
                'name': 'Smallworld'
            }
        )

        self.assertEqual(response.status_code, 401)

        response = self.client.post(
            reverse('login'),
            {
                'username': 'test',
                'password': 'testing'
            }
        )
        token = response.data['token']

        response = self.client.post(
            reverse('boardgame-list'),
            {
                'name': 'Smallworld',
                'editor': self.editor.id
            },
            HTTP_AUTHORIZATION='JWT '+token
        )
        self.assertEqual(response.status_code, 201)

        self.assertEqual(BoardGame.objects.count(), 1)

        boardGame = BoardGame.objects.first()
        self.assertEqual(boardGame.name, 'Smallworld')

