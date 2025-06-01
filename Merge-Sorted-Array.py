def merge(A, B):
        lB=len(B)
        
        for i in range(abs(lB)):
            A.append(0)
        print(A)
        lA=len(A)
        
        i,j,k=lA-lB-1,lB-1,-1
        while(i>=0 and j>=0):
            if A[i]>B[j]:
                A[k]=A[i]
                i-=1
                k-=1
            else :
                A[k]=B[j]
                j-=1
                k-=1
        while(i>=0):
            A[k]=A[i]
            i-=1
            k-=1
            
        while(j>=0):
            A[k]=B[j]
            j-=1
            k-=1
        return A    
        
A=[-4,3]
B=[-2,-2]
merge(A,B)
print(A)