def findprime(l,s,sum):
    prime=[True for i in range(sum+1)]

    prime[0]=False
    prime[1]=False

    p=2
    while(p**2<=sum):
        if prime[p]==True:
            for i in range(p**2,sum+1,p):
                prime[i]=False
        p+=1

    for i in range(s,sum+1):
        if prime[i]==True:
            l.append(i)

def findsumutil(arr,i,sum,path,n,N):

    if sum==0 and len(path)==n:
        print(path)
        return

    if sum<0 or i>=N:
        return

    path.append(arr[i])

    findsumutil(arr,i+1,sum-arr[i],path,n,N)

    path.pop()

    findsumutil(arr,i+1,sum,path,n,N)




def findsum(n,p,sum):
    arr=[]
    findprime(arr,p,sum)

    N=len(arr)

    path=[]

    findsumutil(arr,0,sum,path,n,N)


S = 54
N = 2
P = 3
findsum(N,P,S)
