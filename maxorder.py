def len(arr,n):
	m=1
	l=1
	for i in range(1,n):
		if arr[i] > arr[i-1]:
			l=l+1
		else:
			if m<l:
				m=l
			l=1
	if m<l:
		m=l
	return m
n=int(input())
lst=list(map(int,input().split()))
print(len(lst,n))
