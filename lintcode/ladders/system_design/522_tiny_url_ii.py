import random


class TinyUrl2:
    """
    @param: long_url: a long url
    @param: key: a short key
    @return: a short url starts with http://tiny.url/
    """

    def __init__(self):
        self.short2long = {}
        self.long2short = {}

    def createCustom(self, long_url, key):
        # write your code here
        short = "http://tiny.url/" + key
        if short in self.short2long and self.short2long[short] != long_url:
            return "error"
        if long_url in self.long2short and self.long2short[long_url] != short:
            return "error"
        self.long2short[long_url] = short
        self.short2long[short] = long_url
        return short

    """
    @param: long_url: a long url
    @return: a short url starts with http://tiny.url/
    """

    def longToShort(self, long_url):
        # write your code here
        if long_url in self.long2short:
            return self.long2short[long_url]
        short = self.generate_short()
        while short in self.short2long:
            short = self.generate_short()
        self.short2long[short] = long_url
        self.long2short[long_url] = short
        return short

    """
    @param: short_url: a short url starts with http://tiny.url/
    @return: a long url
    """

    def shortToLong(self, short_url):
        # write your code here
        if short_url not in self.short2long:
            return "error"
        return self.short2long[short_url]

    def generate_short(self):
        CHARS = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        LENS = 6
        short = ""
        for _ in range(LENS):
            short += random.choice(CHARS)
        return "http://tiny.url/" + short


"""
The description is not very clear when there is a collision customizing url
It turns out, whenever there is an collision as long as the record in db is different
from the customization it is an error
"""
