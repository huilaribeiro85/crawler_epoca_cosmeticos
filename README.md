* necessary git on environment variable
* necessary pip on environment variable

- command to install lib from git:
pip install git+https://github.com/huilaribeiro85/crawler_epoca_cosmeticos.git

- create a py with this content to run:

from crawler_epoca_cosmeticos.crawler.crawler_epoca_cosmeticos import CrawlerEpocaCosmeticos

CrawlerEpocaCosmeticos().run()

