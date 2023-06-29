def Queue():
    queue=[]
    return queue
def isEmpty(queue):
    return len(queue)==0
def Enqueue(queue,x):
    queue.append(x)
def Dequeue(queue):
    return queue.pop(0)
def Size(queue):
    return len(queue)

def isparenthesis(c):
    return (c=='c')or (c==')')

def isvalid(s):
    c=0
    for i in range(len(s)):
        if s[i]=='(':
            c+=1
        elif s[i]==')':
            c-=1

        if c<0:
            return False
    return c==0

def removeinvalid(s):
    vis=set()
    queue=Queue()
    level=False

    Enqueue(queue,s)
    while(Size(queue)):
        s=Dequeue(queue)

        if isvalid(s):

            print(s)

            level=True

        if level==True:
            continue

        for i in range(len(s)):

            if (not isparenthesis(s[i])):
                continue

            temp=s[0:i]+s[i+1:]

            if temp not in vis:
                vis.add(temp)
                Enqueue(queue,temp)

removeinvalid("()())()")



