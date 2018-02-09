# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class UserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    name = Field()
    avatar_url = Field()
    user_type = Field()
    url_token = Field()
    url = Field()
    type = Field()
    is_org = Field()
    is_following = Field()
    is_followed = Field()
    is_advertiser = Field()
    headline = Field()
    gender = Field()
    follower_count = Field()
    badge = Field()
    avatar_url_template = Field()
    articles_count = Field()
    answer_count = Field()

