class Solution():
  def coverPoints(self,A,B):
    a=[]
    for i in range(len(A)):
        a.append((A[i],B[i]))
    maxpath=4444444
    def min(a,p):
        dis=[[444444,4444]]
        for j in range(len(a)):
            dx=abs(p[0]-a[j][0])
            dy=abs(p[1]-a[j][1])
            if (dx+dy)!=0:
                if dx>dy :
                  if dx<dis[0][0]:
                    dis[0][0]=dx
                    dis[0][1]=j
                  
                else :
                  if dy<dis[0][0]:
                    dis[0][0]=dy
                    dis[0][1]=j
                
        return dis
    steps=4444
    for i in range(len(a)):
        p=a
        count=0
        start=a[i]
        p=[i for i in a if i!=start]
        for j in range(len(a)-1):
            c=min(p,start)
            count+=c[0][0]
            start=p[c[0][1]]
            p=[i for i in p if p!=start]
            if count>steps:
                break
        if count<steps:
            steps=count

    return steps

A = [ 4, 8, -7, -5, -13, 9, -7, 8 ]
B = [ 4, -15, -10, -3, -13, 12, 8, -8 ]
ss=Solution()
print(ss.coverPoints(A,B))

