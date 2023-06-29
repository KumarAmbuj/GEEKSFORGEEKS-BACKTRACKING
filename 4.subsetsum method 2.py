def findsubset(arr,sum,n,path):
    if sum==0:
        return True
    if sum<0:
        return False

    for i in range(n):
        path.append(arr[i])
        if findsubset(arr,sum-arr[i],n,path):
            return True
        path.pop()
        sum=sum-arr[i]

def find(arr,sum,n):
    path=[]
    if findsubset(arr,sum,n,path):
        print(path)

weights = [15, 22, 14, 26, 32, 9, 16, 8]
target = 53
find(weights,target,len(weights))
