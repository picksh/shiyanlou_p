#!/usr/bin/env python3

import sys
try:
    
    a=int(sys.argv[1])
    b=a-3500
    if a<=3500:
        print(format(0,"0.2f"))
    elif b<=1500:
        print(format(0.03*b,".2f"))
    elif b<=4500:
        print(format(0.1*b-105,".2f"))
    elif b<=9000:
        print(format(0.2*b-555,"0.2f"))
    elif b<=35000:
        print(format(0.25*b-1005,"0.2f"))
    else:
        print(format(0.3*b-2755,"0.2f"))
except:
    print("Parameter Error")


