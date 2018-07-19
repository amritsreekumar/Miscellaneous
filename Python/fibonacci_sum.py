#!/bin/usr/env python
limit = int(input())
first, second = 0,1
sum1 = 2
if limit == 1:
	print('1')
elif limit == 2:
	print('2')
else:
	for i in range (2,limit):
		temp = first + second
		first = second
		second = temp
		sum1 = sum1 + second
print(int(sum1))

