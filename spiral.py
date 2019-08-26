class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        n=int(A)
        lastc=n
        lastr=n
        i=0 #starting row
        j=0 #starting column
        result=[[0 for i in range(n)] for i in range(n)]
        count=1
        while (i<lastr and j<lastc):
            
            for p in range(j,lastc):
               result[i][p]=count
               count+=1
            i+=1
            for p in range(i,lastr):
                result[p][lastc-1]=count
                count+=1
            lastc-=1
            
            if i<lastr:
                t=lastc-1
                while t >= j:
                    result[lastr-1][t]=count
                    count+=1
                    t-=1
                lastr-=1
            
            if j<lastc:
                t=lastr-1
                while t>=i:
                    result[t][j]=count
                    count+=1
                    t-=1
                j+=1
          
        return result
        
                    
s=Solution()
a=10
x=s.generateMatrix(a)
for i in range(len(x)):
    print(x[i])