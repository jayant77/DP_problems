def cont_dp(arr):
	summ=[0]*len(arr)
	if arr[0]>0:
		summ[0]=arr[0]
	else:
		summ[0]=0
	for i in range(1,len(arr)):
		if arr[i]+summ[i-1]>0:
			summ[i]=arr[i]+summ[i-1]
		else:
			summ[i]=0
	x=max(summ)
	return x
arr=[1,2,3,-7,2,5,7,8,2,0,1,-4]
print(cont_dp(arr))