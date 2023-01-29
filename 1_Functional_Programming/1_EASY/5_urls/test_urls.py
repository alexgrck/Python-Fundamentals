import unittest
from urls import shrunk_url, domain_of_url, url_list


class TestCountDays(unittest.TestCase):
 
    def test_shrunk_url(self):
        test_url_1 = 'http://amazon.co.uk'
        test_url_2 = 'https://amazon.co.uk'
        test_url_3 = 'ftp://public.ftp-servers.example.com'
        self.assertEqual(shrunk_url(test_url_1), 'amazon.co.uk')
        self.assertEqual(shrunk_url(test_url_2), 'amazon.co.uk')
        self.assertEqual(shrunk_url(test_url_3), 'public.ftp-servers.example.com')
    
    def test_domain_of_url(self):
        test_url_1 = 'https://example.amazon.co.uk'
        test_url_2 = 'ftp://public.ftp-servers.example.com'
        self.assertEqual(domain_of_url(test_url_1), 'amazon.co.uk')
        self.assertEqual(domain_of_url(test_url_2), 'example.com')

    def test_url_list(self):
        test_url_1 = 'https://www.programiz.com/python-programming/global-keyword'
        test_url_2 = 'ftp://public.ftp-servers.example.com'
        test_url_3 = 'https://www.gov.uk/government/statistical-data-sets/unclaimed-estates-list'
        self.assertEqual(url_list(test_url_1), ['https://', 'www', 'programiz', 
            'com', 'python-programming', 'global-keyword'])
        self.assertEqual(url_list(test_url_2), ['ftp://', 'public', 'ftp-servers', 
            'example', 'com'])
        self.assertEqual(url_list(test_url_3), ['https://', 'www', 'gov', 
            'uk', 'government', 'statistical-data-sets', 'unclaimed-estates-list'])

