from django.contrib.auth import get_user_model

from snippets.models import Snippet

from django.test import TestCase


class TestsTwo(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='root', password='admin')
        self.client.login(username='root', password='admin')
        self.user.save()
        self.snippet = Snippet(
            title='snip3',
            code='snip3',
            owner=self.user)
        self.snippet.save()

    def tearDown(self):
        self.snippet.delete()

    def test_view_all_snips(self):
        response = self.client.get('/api/snippets/')
        self.assertEqual(response.status_code, 200)

    def test_add_snip(self):
        response = self.client.post('/api/snippets/', data={
            'title': 'snip4',
            'code': 'snip4',
            'linenos': False,
            'language': 'python',
            'style': 'friendly',
            'owner': self.user
        })
        self.assertEqual(response.status_code, 201)
