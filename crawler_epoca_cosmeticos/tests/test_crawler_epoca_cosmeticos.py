import os
import unittest
from crawler.crawler_epoca_cosmeticos import CrawlerEpocaCosmeticos


class TestCrawlerEpocaCosmeticos(unittest.TestCase):
    def test_get_site_content(self):
        cec = CrawlerEpocaCosmeticos(os.getcwd())
        ret = cec.get_site_content("https://www.epocacosmeticos.com.br")
        self.assertTrue(ret)

    def test_get_product_by_page(self):
        cec = CrawlerEpocaCosmeticos(os.getcwd())
        ret = cec.get_product_by_page("/buscapagina?fq=C%3a%2f1000001%2f&PS=50&"
                                         "sl=f804bbc5-5fa8-4b8b-b93a-641c059b35b3&cc=4&sm=0&PageNumber=", 1)
        self.assertEqual(type(ret), list)

    def test_get_categories(self):
        cec = CrawlerEpocaCosmeticos(os.getcwd())
        ret = cec.get_categories()
        self.assertTrue(ret)

    def test_get_product_info(self):
        cec = CrawlerEpocaCosmeticos(os.getcwd())
        ret = cec.get_product_info("https://www.epocacosmeticos.com.br/amor-amor-eau-de-toilette-cacharel-perfume-feminino/p")
        self.assertTrue(ret)

    def test_create_csv(self):
        cec = CrawlerEpocaCosmeticos(os.getcwd())
        ret = cec.create_csv(["test1", "test2", "test3"])
        os.remove("product_infos.csv")
        self.assertTrue(ret)


if __name__ == '__main__':
    unittest.main()
