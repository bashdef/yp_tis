from django.contrib.auth import get_user_model

from snippets.models import Snippet

from django.test import TestCase


class TestThree(TestCase):

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

    def test_view_one_snip(self):
        response = self.client.get('/api/snippets/1')
        self.assertEqual(response.status_code, 301)

    def test_update_snip(self):
        response = self.client.patch('/api/snippets/1', data={
            'title': 'snip4'},
                                     content_type='application/json')
        self.assertEqual(response.status_code, 301)

    def test_del_snip(self):
        response = self.client.delete('/api/snippets/1')
        self.assertEqual(response.status_code, 301)
