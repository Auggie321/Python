# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Spider, Request
from zhihuuser.items import UserItem

class ZhihuSpider(Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    start_user = 'excited-vczh'

    user_url = 'http://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    follows_url = 'http://www.zhihu.com/api/v4/members/{user}/followees?include{include}&offset={offset}&limit={limit}'
    follows_query = 'ata[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    followers_url = 'http://www.zhihu.com/api/v4/members/{user}/followers?include{include}&offset={offset}&limit={limit}'
    followers_query = 'ata[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'


    def start_requests(self):
#        url = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20'
#        url = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'
#        url = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=80&limit=20'
        yield Request(self.user_url.format(user=self.start_user,include=self.user_query ),self.parse_user)
        yield Request(self.follows_url.format(user=self.start_user, include=self.follows_query, offset=0,limit=20), callback=self.parse_follows)
        yield Request(self.followers_url.format(user=self.start_user, include=self.followers_query, offset=0,limit=20), callback=self.parse_followers)


    def parse_user(self, response):
#        print(response.text)
        result = json.loads(response.text)
        item  = UserItem()
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        yield item
        yield Request(self.follows_url.format(user=result.get('url_token'), include=self.follows_query, limit=20, offset=0), self.parse_follows)



    def parse_follows(self,response):
#        print(response.text)
        results = json.loads(response.text)

        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'),include=self.user_query), self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, self.parse_follows)


def parse_followers(self, response):
    #        print(response.text)
    results = json.loads(response.text)

    if 'data' in results.keys():
        for result in results.get('data'):
            yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query), self.parse_user)

    if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
        next_page = results.get('paging').get('next')
        yield Request(next_page, self.parse_followers)
