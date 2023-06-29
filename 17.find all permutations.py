def findpermuteutil(l,i,n):
    if i==n:
        print(''.join(l))
        return

    j=i
    while(j<n):

        l[i],l[j]=l[j],l[i]

        findpermuteutil(l,i+1,n)

        l[i],l[j]=l[j],l[i]
        j+=1






def findpermute(s,n):
    l=list(s)
    findpermuteutil(l,0,n)

string = "ABC"

findpermute(string,3)