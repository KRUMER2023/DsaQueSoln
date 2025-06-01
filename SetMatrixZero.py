# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output:         [[1,0,1],[0,0,0],[1,0,1]]

# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

def setZeroes( a):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(a)
        m=len(a[0])
        for i in range(n):
            for j in range(m):
                if a[i][j] ==0:
                    # change row to "*" where 0 is present except 0 itself
                    for x in range(n):
                        if a[x][j]!=0:
                            a[x][j]='*'
                            
                    # change row to "*" where 0 is present except 0 itself
                    for x in range(m):
                        if a[i][x]!=0:
                            a[i][x]='*'
        # change "*" to 0
        for i in range(n):
            for j in range(m):
                if a[i][j]=="*":
                    a[i][j]=0
        print(a)
                
setZeroes([[1,1,1],[1,0,1],[1,1,1]])