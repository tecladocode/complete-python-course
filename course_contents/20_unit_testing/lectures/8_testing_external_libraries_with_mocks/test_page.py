from page import PageRequester
from unittest import TestCase
from unittest.mock import patch


class TestPageRequester(TestCase):
    def setUp(self):
        self.page = PageRequester('https://google.com')

    def test_make_request(self):
        with patch('requests.get') as mocked_get:
            self.page.get()
            mocked_get.assert_called()
    
    def test_content_returned(self):
        class FakeResponse:
            def __init__(self):
                self.content = 'Hello'

        with patch('requests.get', return_value=FakeResponse()) as mocked_get:
            result = self.page.get()
            self.assertEqual(result, 'Hello')
