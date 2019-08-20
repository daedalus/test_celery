from __future__ import absolute_import, print_function
import os
import sys
import time
from .tasks import *

results = []

if __name__ == '__main__':

    results.append(prime_factors.delay(600851475143))
    results.append(longtime_add.delay(1,2))
    results.append(longtime_add.delay(2,3))
    results.append(fibonacci.delay(10))
    results.append(fibonacci.delay(20))
    results.append(longtime_add.delay(3,4))
    results.append(longtime_add.delay(4,5))
    
    l = len(results)
    while l > 0:
        time.sleep(1)
        print("Main task waiting...")
        for i in range(0,l):
            try:
                if results[i].ready():
                    print("Task: %s, %s" % (str(results[i]),str(results[i].result)))
                    del results[i]
            except:
                pass
        l = len(results)
        #print(results,l)
