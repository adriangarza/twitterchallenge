import sys
import os
from kraken import krakenCount

_m = int(raw_input())
_n = int(raw_input())

for row in krakenCount(_m, _n):
    print row
