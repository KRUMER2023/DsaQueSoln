def intersect(A, B):
    i = j = 0
    result = []

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            result.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1

    return result
        
       
A= [1, 2 ,3, 3, 4, 5, 6]
B=[3,5,8]
print(intersect(A,B))