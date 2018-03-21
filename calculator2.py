#!/usr/bin/env python3

import sys


def cal_insurence(income):
    return income*0.165

def cal_tax(a):
    b=a-3500
    if a<=3500:
        ans=0
    elif b<=1500:
        ans=0.03*b
    elif b<=4500:
        ans=0.1*b-105
    elif b<=9000:
        ans=0.2*b-555
    elif b<=35000:
        ans=0.25*b-1005
    else:
        ans=0.3*b-2755
    return ans

if __name__=="__main__":
    for arg in sys.argv[1:]:
        try:
            number=arg.split(':')
           # print(number[0],number[1])
            temp=int(number[1])-cal_insurence(int(number[1]))
           # print(temp)
            total=format(temp-cal_tax(temp),".2f")
           # print("total=",total)
            print('{}:{}'.format(number[0],total))
        except:
            print("Parameter Error")
 
