from django.contrib.auth import get_user_model

from .models import Snippet

from django.test import TestCase


class TestsOne(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testUser', password='qweasd')
        self.client.login(username='testUser', password='qweasd')
        self.user.save()
        self.snippet = Snippet(
            title='title',
            code='asd',
            owner=self.user)
        self.snippet.save()

    def test_read_snippet(self):
        self.assertEqual(self.snippet.title, 'title')
        self.assertEqual(self.snippet.code, 'asd')
        self.assertEqual(self.snippet.owner, self.user)

    def test_update_snip_description(self):
        self.snippet.title = 'new title'
        self.snippet.save()
        self.assertEqual(self.snippet.title, 'new title')

    def test_del_snip(self):
        self.snippetDel = self.snippet.delete()
        self.assertEqual(self.snippetDel, (1, {'snippets.Snippet': 1}))


class TestsTwo(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testUser', password='qweasd')
        self.client.login(username='testUser', password='qweasd')
        self.user.save()
        self.snippet = Snippet(
            title='title',
            code='asd',
            owner=self.user)
        self.snippet.save()

    def tearDown(self):
        self.snippet.delete()

    def test_view_all_snips(self):
        response = self.client.get('/api/snippets/')
        self.assertEqual(response.status_code, 200)

    def test_add_snip(self):
        response = self.client.post('/api/snippets/', data={
            'title': 'qwe',
            'code': 'asd',
            'linenos': False,
            'language': 'python',
            'style': 'friendly',
            'owner': self.user
        })
        self.assertEqual(response.status_code, 201)


class TestThree(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testUser', password='qweasd')
        self.client.login(username='testUser', password='qweasd')
        self.user.save()
        self.snippet = Snippet(
            title='title',
            code='asd',
            owner=self.user)
        self.snippet.save()

    def tearDown(self):
        self.snippet.delete()

    def test_view_one_snip(self):
        response = self.client.get('/api/snippets/1')
        self.assertEqual(response.status_code, 301)

    def test_update_snip(self):
        response = self.client.patch('/api/snippets/1', data={
            'title': 'loremipsum'},
            content_type='application/json')
        self.assertEqual(response.status_code, 301)

    def test_del_snip(self):
        response = self.client.delete('/api/snippets/1')
        self.assertEqual(response.status_code, 301)