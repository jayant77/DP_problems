def fibo_dp(n):
	arr=[]
	arr.append(0)
	arr.append(1)
	if n==0 or n==1:
		return arr[n]
	else:
		for i in range(2,n+1):
			arr.append(arr[i-1]+arr[i-2])
	return arr[n]
def fact(n):
	if n==0:
		return 1
	else:
		arr=[]
		arr.append(1)
		for i in range(0,n):
			arr.append((i+1)*arr[i])
	return arr[n]
n=int(input())
print(fibo_dp(n))
print(fact(n))