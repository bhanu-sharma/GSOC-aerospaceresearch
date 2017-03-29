""" A simple task scheduler """
import random
import time 
from datetime import datetime as dt 
#import collections
#import threading
#import sched

def number_generator(n):
    """ A co-routine that generates numbers in range 1..n """

    for i in range(1, n+1):
        return i

def square_numbers(numbers):
    """ A co-routine task for converting numbers to squares """

    for n in numbers:
        return n*n
def tuning_band(frequency):
    ''' It will tune to the frequency mentioned '''
    pass
def scan(band):
    '''It will scan the 1090mhz band '''
    pass

if __name__ == "__main__":
    # d is the dictionary in which the time to schedule the function is the key and value is the frequency for function tuning_band
    d = {"hh1:mm1:ss1:000000" : "f1",
         "hh2:mm2:ss2:000000" : "f2",
         "hh3:mm3:ss3:000000" : "f3"}
    while True:
        if str(dt.utcnow().time()) == "hh:mm:ss:000000":
            print number_generator(6)
            continue
        if str(dt.utcnow().time()) == "hh:mm:ss:000000":
            print squares_numbers(2)
            continue 
        if str(dt.utcnow().time()) == "hh1:mm1:ss1:000000":
            print tuning_band(d["hh1:mm1:ss1:000000"])
            continue
        else:
            scan(1090)
