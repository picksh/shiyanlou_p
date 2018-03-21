#!/usr/bin/env python3

import sys
import csv
import os


class Args(object):
	def __init__(self):
		self.args=sys.argv[1:]
	def get_config(self):
		indexofconfig=args.index('-c')+1
		if os.path.exists(args[indexofconfig])==False
			raise ValueError()
		return args[indexofconfig]
	def get_input(self):

		indexofinput=args.index('-d')+1
		if os.path.exists(args[indexofinput])==False
			ra
		return args[indexofinput]
	def get_output(self):

		indexofoutput=args.index('-o')+1
		return args[indexofoutput]
		

class Config(object):
	def __init__(self):
		self.config=self._read_config()
	
	def _read_config(self):
		config={}

class UserData(object):
	def __init__(self):
		self.usrdata=self._read_users.data()

	def _read_users_data(self):
		userdata=[]
	
class IncomeTaxCalculator(object):
	def calc_for_all_userdata(self):

	def export(self,default='csv'):
		result =self.calc_for_all_userdata()
		with open("") as f:
			writer=csv.writer(f)
			writer.writerows(result)

if __name__=='__main__':
			
    			

def cal_insurence(income)
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
	
	except ValueError:
		print("Parameter Error")
