import scrapy


class QuotesSpider(scrapy.Spider):
    name = "comments"

    def start_requests(self):
        urls = [
            'file:///Users/sur000e/workspace-mallet/walmart/input/1.html',
            # 'https://www.consumeraffairs.com/retail/walmart.htm?page=2',
            # 'https://www.consumeraffairs.com/retail/walmart.htm?page=3',
            # 'https://www.consumeraffairs.com/retail/walmart.htm?page=4',
            # 'https://www.consumeraffairs.com/retail/walmart.htm?page=5',
            # 'https://www.consumeraffairs.com/retail/walmart.htm?page=6',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

            def parse(self, response):
                page = 1
                for comment in response.xpath('//div[@class="review-body__text"]/p').extract():
                    filename = 'comment-%s.txt' % page
                    page = page + 1
                    with open(filename, 'wb') as f:
                        f.write(comment)
                        self.log('Saved file %s' % filename)
