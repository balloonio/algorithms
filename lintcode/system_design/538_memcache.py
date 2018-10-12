class Memcache:
    def __init__(self):
        # do intialization if necessary
        self.key2value = {}
        self.key2expire = {}
        self.expire2keys = collections.defaultdict(set)

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: An integer
    """

    def get(self, curtTime, key):
        # write your code here
        self.check_expire(curtTime)
        if key not in self.key2value:
            return 2147483647
        return self.key2value[key]

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: value: An integer
    @param: ttl: An integer
    @return: nothing
    """

    def set(self, curtTime, key, value, ttl):
        # write your code here
        self.check_expire(curtTime)
        self.delete(curtTime, key)
        self.key2value[key] = value
        if ttl:
            self.expire2keys[curtTime + ttl].add(key)
            self.key2expire[key] = curtTime + ttl

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: nothing
    """

    def delete(self, curtTime, key):
        # write your code here
        self.check_expire(curtTime)
        if key not in self.key2value:
            return
        self.key2value.pop(key)
        if key not in self.key2expire:
            return
        exp = self.key2expire.pop(key)
        self.expire2keys[exp].remove(key)

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """

    def incr(self, curtTime, key, delta):
        # write your code here
        self.check_expire(curtTime)
        if key not in self.key2value:
            return 2147483647
        self.key2value[key] += delta
        return self.key2value[key]

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """

    def decr(self, curtTime, key, delta):
        # write your code here
        self.check_expire(curtTime)
        if key not in self.key2value:
            return 2147483647
        self.key2value[key] -= delta
        return self.key2value[key]

    def check_expire(self, curtTime):
        if curtTime in self.expire2keys:
            keys = self.expire2keys[curtTime]
            for key in keys:
                self.key2value.pop(key)
                self.key2expire.pop(key)
            self.expire2keys.pop(curtTime)


# pay attention that set key can refresh time
# pay attention that key might not have an entry in key2expire
