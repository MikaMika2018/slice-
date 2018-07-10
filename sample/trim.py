#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 利用切片操作，实现一个trim()函数，去掉字符串首尾的空格，输出字符串，不能使用str的strip()方法。
def trim(s):
	if s[:1].isspace():
		s=s[1:]
		return trim(s)
	elif s[-1:].isspace():
		s=s[:-1]
		return trim(s)
	else:
		return s

a=trim('hello ')
b=trim(' hello')
d=trim('     ')
e=trim(' hello ')
print('a=',a,'b=',b,'d=',d,'e=',e)
if trim('hello ')=='hello':
	print('1 pass!')
if trim(' hello')=='hello':
	print('2 pass!')
if trim(' hello ')=='hello':
	print('3 pass!')
if trim('  ')=='':
	print('4 pass!')
if trim('    ')=='':
	print('5 pass!')
else:
	print('fail!')
