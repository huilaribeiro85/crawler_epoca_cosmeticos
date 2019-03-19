#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import csv
import requests


class CrawlerEpocaCosmeticos:
    def __init__(self, log_path):
        self.site = "https://www.epocacosmeticos.com.br"
        self.log_path = os.path.join(log_path, 'product_infos.csv')
        self.unique_product_list = list()

    def get_site_content(self, site):
        site_open = requests.get(site)
        if site_open.status_code == 200:
            return requests.get(site).text
        return False

    def get_product_by_page(self, partial_search_url, page_number):
        page_url = self.site + partial_search_url + str(page_number)
        page_content = self.get_site_content(page_url)
        return re.findall("(?<=shelf-default__link\" href=\").*(?=\")", page_content)

    def get_categories(self):
        site_content = self.get_site_content(self.site)
        category_body_part = re.findall("(?<=Ver Categorias).*Unhas", site_content)
        category_urls = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
                                   category_body_part[0])
        category_dict = dict()
        for url in category_urls:
            category = url.split("/")[-1]
            category_dict[category] = {"category_url": url}
        return category_dict

    def get_product_info(self, product_url):
        product_url_content = self.get_site_content(product_url)
        page_title = re.findall("(?<=pageTitle\":\").*?(?=\")", product_url_content)
        product_name = re.findall("(?<=productName\":\").*?(?=\")", product_url_content)
        if product_name and page_title:
            return [product_name[0], page_title[0], product_url]
        return False

    def create_csv(self, info_by_product):
        try:
            open_csv = open(self.log_path, 'a+')
            wr = csv.writer(open_csv, delimiter="|", quoting=csv.QUOTE_NONE, quotechar='', lineterminator='\n')
            wr.writerow(info_by_product)
            open_csv.close()
            return True
        except Exception as err:
            print(err)
            return False

    def run(self):
        if os.path.exists(self.log_path):
            os.remove(self.log_path)
        categories = self.get_categories()
        for category, url in categories.items():
            category_content = self.get_site_content(url["category_url"])
            partial_search_url = re.findall("(?<=.load\(').*(?=')", category_content)
            partial_params = partial_search_url[0].split('&')
            partial_params[1] = 'PS=50'
            new_partial_search_url = "&".join(partial_params)

            product_by_page = True
            page_number = 0
            while product_by_page:
                product_by_page = self.get_product_by_page(new_partial_search_url, page_number)
                if product_by_page:
                    for product_url in product_by_page:
                        if product_url not in self.unique_product_list:
                            self.unique_product_list.append(product_url)
                            info_by_product = self.get_product_info(product_url)
                            if info_by_product:
                                print(info_by_product)
                                self.create_csv(info_by_product)
                            else:
                                print(product_url)
                page_number += 1


if __name__ == "__main__":
    cec = CrawlerEpocaCosmeticos(os.getcwd())
    cec.run()
