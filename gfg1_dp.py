t=int(input())
while(t):
    n=int(input())
    arr=[]
    arr.append(n)
    while(arr[len(arr)-1])!=0:
        if arr[len(arr)-1]%2==0:
            arr.append(int(arr[len(arr)-1]/2))
        else:
            arr.append(int(arr[len(arr)-1]-1))
    print(arr)