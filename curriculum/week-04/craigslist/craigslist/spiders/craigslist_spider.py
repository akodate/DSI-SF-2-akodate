from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy

# item models
from craigslist.items import CraigslistItem, CraigslistItemDetail

class CraigslistSpider(CrawlSpider):

  name = "craigslist"
  allowed_domains = ["craigslist.org"]
  start_urls = [
      "http://sfbay.craigslist.org/search/sfc/apa"
  ]

  rules = (
      Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="button next"]',)), callback="parse_search", follow = True),
  #   Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="hdrlnk"]',)), callback="parse_page", follow = True),
  )


  def parse(self, response):
    """
      We will be retiring our parse_search method
    """

    for sel in response.xpath("//p[@class='row']"):

        item = CraigslistItem()
        item['title'] =  sel.xpath("span/span/a[@class='hdrlnk']/span/text()").extract()[0]
        item['link']  =  sel.xpath("span/span/a/@href").extract()[0]
        item['price']  =  sel.xpath("span/span/span[@class='price']/text()").extract()[0]
        yield item

  # def parse_page(self, response):
  #   print "Parsing a detail page!"

  #   item_detail   = CraigslistItemDetail()

  #   extracted = {
  #     "address":    response.xpath("//div[@class='mapaddress']/text()").extract(),
  #     "movein_date":  response.xpath("//span[contains(@class, 'housing_movein_now')]/text()").extract()
  #   }

  #   # Check that our extracted entities are not empty
  #   for entity, extracted in extracted.items():
  #     if len(extracted) > 0:
  #       # if not, extract the first item (expecting single list entities)
  #       item_detail[entity] = extracted[0]

  #   yield item_detail