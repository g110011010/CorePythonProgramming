import sys
argv=sys.argv
def minCoin(coin):
    coins=(1,5,10,25)
    result=[x for x in range(len(coins))]
    num=len(coins)
    while num>0:
        num-=1
        result[num],coin=divmod(coin,coins[num])
    return result
print minCoin(int(argv[1]))
