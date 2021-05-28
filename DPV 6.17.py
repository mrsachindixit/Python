#Problem 6.17 from Dasgupta Book
#6.17. Given an unlimited supply of coins of denominations x1; x2; : : : ; xn, we wish to make change for
#a value v; that is, we wish to find a set of coins whose total value is v. This might not be possible:
#for instance, if the denominations are 5 and 10 then we can make change for 15 but not for 12.
#Give an O(nv) dynamic-programming algorithm for the following problem.
#Input: x1; : : : ; xn; v.
#Question: Is it possible to make change for v using coins of denominations x1; : : : ; xn?
import sys
def minCoins(coins,TargetV):
    coinN=len(coins)
    res= [0]* coinN
    for i in coins:
        print (i)
        if TargetV % i == 0:
            res[coins.index(i)] = 1 
            # we could have returned at the first instance of divisibility but 
            # given that it is dyamic programming we compute all possible cases which will be helpful
            # in solving other varients like 6.18 etc where diff constrains on coin num/usage are applied
    return res.__contains__(1)
coins = [9, 6, 5, 2]

TargetV = 12
print("This combination is possible ",minCoins(coins,  TargetV))
