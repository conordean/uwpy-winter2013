from django.test import TestCase
from uw.models import Activity

class SimpleTest(TestCase):
    def setUp(self):
        Activity(content='This is a test greeting').save()

    def test_setup(self):
        self.assertEqual(1, len(Activity.objects.all()))
        self.assertEqual('This is a test greeting', Activity.objects.all()[0].content)
