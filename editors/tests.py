# -*- coding: utf8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse
# from django.test.utils import setup_test_environment
# setup_test_environment()

# Create your tests here.

from editors.models import Editor
from django.contrib.auth.models import User


class EditorMethodTests(TestCase):

    def test_unicode(self):
        """
        __unicode__() should returns the name of the editor
        """
        editor = Editor(name='Asmodée')
        editor.save()
        self.assertEqual(editor.__unicode__(), 'Asmodée')


class EditorViewTests(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.user = User.objects.create_user(
            username='test', email='test@mail.com', password='testing')

    def test_index(self):
        response = self.client.get(reverse('editor-list'))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.post(reverse('editor-list'),
                                    {'name': 'Black Rock'})
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
            reverse('editor-list'),
            {
                'name': 'Black Rock'
            },
            HTTP_AUTHORIZATION='JWT '+token
        )
        self.assertEqual(response.status_code, 201)

        self.assertEqual(Editor.objects.count(), 1)

        editor = Editor.objects.first()
        self.assertEqual(editor.name, 'Black Rock')
