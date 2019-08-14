no=int(input())
first=0
second=1
for i in range(2,no):
	next=first+second
	print(next,end=" ")
	first=second
	second=next
