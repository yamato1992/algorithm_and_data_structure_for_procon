def insert(x, A = []):
    return list(x) + A

def delete(A, x):
    for i in range(len(A)):
        if A[i] == x:
            A.pop(i)
            return A

def deleteFirst(A):
    return A[1:]

def deleteLast(A):
    return A[:-1]