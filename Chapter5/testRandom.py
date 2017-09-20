import random
class TestRandom(object):
    num=20
    def testRandint(self,a,b):
        n=self.num
        while n>0:
            print random.randint(a,b)
            n-=1
t=TestRandom()
t.testRandint(10,100)
