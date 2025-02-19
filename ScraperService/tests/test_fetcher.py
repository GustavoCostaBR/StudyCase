import unittest
from unittest.mock import patch, MagicMock
from src.fetcher import Fetcher

class TestFetcher(unittest.TestCase):
    @patch('src.fetcher.webdriver.Chrome')
    def test_fetch_html(self, MockChrome):
        mock_driver = MagicMock()
        MockChrome.return_value = mock_driver
        mock_driver.page_source = "<html><body><div class='test-class'>Test Content</div></body></html>"

        fetcher = Fetcher("http://example.com", "test-class")
        html = fetcher.fetch_html()

        self.assertIn("Test Content", html)
        mock_driver.quit.assert_called_once()

if __name__ == '__main__':
    unittest.main()