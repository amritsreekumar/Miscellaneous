'''Once upon a time Professor Idioticideasinventor was travelling by train. 
Watching cheerless landscape outside the window, 
he decided to invent the theme of his new scientific work. 
All of a sudden a brilliant idea struck him: to develop an effective algorithm finding an integer number, 
which is x times less than the sum of all its integer positive predecessors, where number x is given. 
As far as he has no computer in the train, you have to solve this difficult problem.'''

#!/bin/usr/env python
i = int(input())
k= 1
sum1 = 0
while(1):
	sum1 = sum1 + k
	if sum1/i == k+1:
		print(k+1)
		break
	k = k+1

