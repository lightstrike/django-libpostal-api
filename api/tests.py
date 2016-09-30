from django.core.urlresolvers import reverse
from django.test import SimpleTestCase
from rest_framework.test import APIClient


class PostalAPITestMixin():
    view_name = None

    def setUp(self):
        self.client = APIClient()
        self.url = reverse(self.view_name)
        self.address = '123 Postal St, Lib Postal, NY 10001 USA'

    def test_get_with_no_params_returns_400(self):
        response = self.client.get(self.url)
        assert response.status_code == 400

    def test_get_with_address_param_returns_200(self):
        response = self.client.get(self.url, {'address': self.address})
        assert response.status_code == 200

    def test_get_with_address_and_other_params_returns_200(self):
        query_params = {
            'address': self.address,
            'lib': 'postal',
            'city': 'new york',
        }
        response = self.client.get(self.url, query_params)
        assert response.status_code == 200

    def test_get_with_other_params_returns_400(self):
        response = self.client.get(self.url, {'target': self.address})
        assert response.status_code == 400


class ExpandAPIViewTestCase(PostalAPITestMixin, SimpleTestCase):
    view_name = 'expand'


class ParseAPIViewTestCase(PostalAPITestMixin, SimpleTestCase):
    view_name = 'parse'
