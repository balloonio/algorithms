class Iter:
    def __init__(self, arr):
        self.index = 0
        self.arr = arr
    
    def next(self):
        if not self.hasNext():
            raise Exception("No next")
        v = self.arr[self.index]
        self.index+=1
        return v
        
    def hasNext(self):
        return self.index < len(self.arr)
    

class Iter5:
    def __init__(self, given_iter):
        self.iter1 = given_iter
        self.cached_value = None

    def next(self):
        result = self.cached_value
        self.cached_value = None  # fetch resets cached value
        self.hasNext()  # cache the next possible value
        return result
        
    def hasNext(self):
        # already has next and not fetched by next()
        if self.cached_value is not None:
            return True
        
        # self.cached_value already fetched
        while self.iter1.hasNext():
            iter1_val = self.iter1.next()
            if iter1_val % 5 == 0:
                self.cached_value = iter1_val
                break
        
        if self.cached_value:
            return True
    

def test_iter5():
    i = Iter([1,2,3,4, 5, 6, 7,100,0, -5])
    
    i5 = Iter5(i)
    print(i5)
    assert i5.hasNext()
    assert i5.next() == 5
    assert i5.next() == 100
    assert i5.hasNext()
    assert i5.next() == 0
    print("ok")

def test_iter_empty():
    i = Iter([])
    
    i5 = Iter5(i)
    print(i5)
    assert not i5.hasNext()
    print("0k")
    
test_iter5()
test_iter_empty()
