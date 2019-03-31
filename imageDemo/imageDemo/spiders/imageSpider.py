
import scrapy
from scrapy.selector import Selector
from imageDemo.items import ImagedemoItem
from imageDemo.items import MenuImageItem

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class imageSpider(scrapy.Spider):

    name = "imageSpider"
    allowed_domains = ["yelp.com"]

    start_urls = [
        # "https://www.yelp.com/search?cflt=restaurants&find_loc=San%20Francisco%2C%20CA&start=0",
        # "https://www.yelp.com/biz_photos/peoples-bistro-san-francisco-4?tab=menu",
        "https://www.yelp.com/biz_photos/peter-luger-brooklyn-2?tab=menu",
    ]

    def parse(self, response):
        sel = Selector(response)

        menuList = sel.xpath('//*[@id="super-container"]/div[2]/div/div[2]/div[2]/ul/li/div/img/@src').extract()
        print menuList
        # print '>>>>>>>'
        yield MenuImageItem(image_urls=menuList, image_name='peter-luger')

        # list = sel.xpath('//*[@id="wrap"]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/ul/li/div/div/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/h3/a[@class="lemon--a__373c0__IEZFH link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5"]/text()').extract()
        # print list
        # for item in list:
        #     print item
        #     print '>>>>>'
            # yield ImagedemoItem(name=item)
