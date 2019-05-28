def LongIncSubseq(arr):
	tenp=[1]
	#print(type(tenp))
	for i in range(1,len(arr)):
		tenp.append(1)
		#print(arr,tenp)
		for j in range(0,i):
			if arr[i]>arr[j] and tenp[i]<=tenp[j]:
				tenp[i]=tenp[j]+1
	print(tenp)
	return max(tenp)
arr=[3,2,6,4,5,1]
print(LongIncSubseq(arr))