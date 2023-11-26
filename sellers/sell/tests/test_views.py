from django.test import TestCase
from django.urls import reverse
from django.conf import settings
# settings.configure(DATABASES='your_database_settings')


class TestViews(TestCase):

    def test_register_producer_view(self):
        # Use the reverse function to get the URL for your view
        url = reverse('register_producer')

        # Simulate a GET request to the view
        response = self.client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
