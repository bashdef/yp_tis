from django.contrib.auth import get_user_model

from snippets.models import Snippet

from django.test import TestCase


class TestsOne(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='root', password='admin')
        self.client.login(username='root', password='admin')
        self.user.save()
        self.snippet = Snippet(
            title='snip3',
            code='snip3',
            owner=self.user)
        self.snippet.save()

    def test_read_snippet(self):
        self.assertEqual(self.snippet.title, 'snip3')
        self.assertEqual(self.snippet.code, 'snip3')
        self.assertEqual(self.snippet.owner, self.user)

    def test_update_snip_description(self):
        self.snippet.title = 'snip4'
        self.snippet.save()
        self.assertEqual(self.snippet.title, 'snip4')

    def test_del_snip(self):
        self.snippetDel = self.snippet.delete()
        self.assertEqual(self.snippetDel, (1, {'snippets.Snippet': 1}))
