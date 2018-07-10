#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def findMinandMax(L):
	if L==[]:
		return(None,None)
	max=L[0]
	min=L[0]
	for i in L:
		if i > max:
			max = i
		elif i < max:
			min = i
	return(min,max)

a=findMinandMax([5,4,6,7,1,8,9])
print(a)
