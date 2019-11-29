# -*- coding: utf-8 -*-
import scrapy


class FinancebotSpider(scrapy.Spider):
    name = 'financebot'
    #allowed_domains = ['finance.naver.com']
    #start_urls = ['http://finance.naver.com/item/sise_day.nhn?code=005930&page=1']
    start_urls = ['https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001']
    
    def parse(self, response):

        #day = response.xpath('/html/body/table[1]/tbody/tr[3]/td[1]/span').extract()
        #closingPrice = response.xpath('/html/body/table[1]/tbody/tr[3]/td[2]/span').extract()
        #timePrice = response.xpath('/html/body/table[1]/tbody/tr[3]/td[4]/span').extract()
        #volume = response.xpath('/html/body/table[1]/tbody/tr[3]/td[7]/span').extract()
        
        titles = response.xpath('//*[@id="main_content"]/div[2]/ul[1]/li[1]/dl/dt[2]/a').extract()
        authors = response.css('.writing::text').extract()

        #for item in zip(day, closingPrice, timePrice, volume):
        for item in zip(titles, authors):
            scraped_info = {
                #'day': item[0].strip(),
                #'closingPrice': item[1].strip(),
                #'timePrice': item[2].strip(),
                #'volume': item[3].strip(),
                'titles': item[0].strip(),
                'authors': item[1].strip(),
            }
            yield scraped_info

