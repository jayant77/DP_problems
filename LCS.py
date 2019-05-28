def lcs_rec(x,y):
	if not x or not y:
		return ""
	a,b,c,d=x[0],x[1:],y[0],y[1:]
	if a==c:
		return a+lcs_rec(b,d)
	else:
		return(max(lcs_rec(x,d),lcs_reckmid(b,y)))
#print(lcs_rec("abcd","abcd"))
def LCS_dp(x,y):
	arr=[[0 for j in range(len(y)+1)]for i in range(len(x)+1)]
	for i,p in enumerate(x):
		print i,p
		for j,q in enumerate(y):
			if p==q:
				arr[i+1][j+1]=arr[i][j]+1
			else:
				arr[i+1][j+1]=max(arr[i+1][j],arr[i][j+1])
	result=""
	while i!=0 and j!=0:
		print(i,j,result)
		if arr[i][j]==arr[i-1][j]:
			i=i-1
		elif arr[i][j]==arr[i][j-1]:
			j=j-1
		else:
			#assert x[i-1]==y[j-1]
			result=x[i-1]+result
			i=i-1
			j=j-1
	return result
def LiCS_dp(x,y):
	arr=[[0 for j in range(len(y)+1)]for i in range(len(x)+1)]
	for i,p in enumerate(x):
		print i,p
		for j,q in enumerate(y):
			if p<q:
				arr[i+1][j+1]=arr[i][j]+1
			else:
				arr[i+1][j+1]=max(arr[i+1][j],arr[i][j+1])
	result=[]
	while i!=0 and j!=0:
		#print(i,j,result)
		if arr[i][j]==arr[i-1][j]:
			i=i-1
		elif arr[i][j]==arr[i][j-1]:
			j=j-1
		else:
			#assert x[i-1]==y[j-1]
			result.append(x[i-1])
			i=i-1
			j=j-1
	return arr,result
x=[0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
print(LiCS_dp(x,x))
