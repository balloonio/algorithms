import random


class TinyUrl:
    """
    @param: url: a long url
    @return: a short url starts with http://tiny.url/
    """

    def __init__(self):
        self.long2id = {}
        self.id2long = {}

    def longToShort(self, url):
        # write your code here
        if url in self.long2id:
            urlid = self.long2id[url]
            short = self.urlid_to_short(urlid)
            return short
        urlid = random.randint(0, 62 ** 6 - 1)
        while urlid in self.id2long:
            urlid = random.randint(0, 62 ** 6 - 1)
        self.long2id[url] = urlid
        self.id2long[urlid] = url
        return self.urlid_to_short(urlid)

    """
    @param: url: a short url starts with http://tiny.url/
    @return: a long url
    """

    def shortToLong(self, url):
        # write your code here
        urlid = self.short_to_urlid(url)
        if urlid not in self.id2long:
            return None
        return self.id2long[urlid]

    def short_to_urlid(self, short):
        short = short[-6:]
        urlid = 0
        for ch in short:
            urlid *= 62
            urlid += self.digit_62_to_dec(ch)
        return urlid

    def urlid_to_short(self, urlid):
        short = ""
        while urlid:
            short = self.digit_dec_to_62(urlid % 62) + short
            urlid //= 62
        while len(short) != 6:
            short = "0" + short
        return "http://tiny.url/" + short

    # dec : int; return : str char
    def digit_dec_to_62(self, dec):
        if dec >= 62 or dec < 0:
            return None
        if dec >= 0 and dec <= 9:
            return str(dec)
        char_offset = dec - 10
        if char_offset >= 0 and char_offset <= 25:
            return chr(ord("a") + char_offset)
        char_offset -= 26
        return chr(ord("A") + char_offset)

    # char62 : str char; return int
    def digit_62_to_dec(self, char62):
        if len(char62) != 1:
            return None
        if char62 in "0123456789":
            return int(char62)
        if char62 >= "a" and char62 <= "z":
            return 10 + ord(char62) - ord("a")
        if char62 >= "A" and char62 <= "Z":
            return 36 + ord(char62) - ord("A")
        return None
