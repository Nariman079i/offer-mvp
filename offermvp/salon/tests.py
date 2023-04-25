from django.db.models import QuerySet
from django.test import TestCase
from rest_framework.reverse import reverse
from .models import *
from rest_framework.test import APIClient,APIRequestFactory


class MyTest(TestCase):
    def setUp(self):
        FeedBack.objects.create(
            title="Nariman",
            surname="Нариман",
            name="Ибрагим",
            message="Hello world",
        )
        self.feed: QuerySet['FeedBack'] = FeedBack.objects.get(pk=1)
        self.resp = APIRequestFactory()

    def test_feed(self):
        out_put = self.resp.get(reverse('main-page'))
        self.assertEqual(out_put, 'Ибрагим')

    def test_message_len(self):
        self.assertEqual(len(self.feed.name), 7)

