def findsubset(arr,sum,i,n,path):
    if sum==0:
        return True
    if sum<0 or i>=n:
        return False

    path.append(arr[i])
    if findsubset(arr,sum-arr[i],i+1,n,path):
        return True
    path.pop()
    if findsubset(arr,sum,i+1,n,path):
        return True



def find(arr,sum,n):
    path=[]
    if findsubset(arr,sum,0,n,path):
        print(path)
    else:
        print('not possible')

weights = [15, 22, 14, 26, 32, 9, 16, 8]
target = 53
find(weights,target,len(weights))