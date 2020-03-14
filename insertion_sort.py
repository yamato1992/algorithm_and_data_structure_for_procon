def insertion_sort(A, N):
    for i in range(1, N):
        v = A[i]
        j = i - 1
        print(A)
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v

N = int(input())
A = list(map(int, input().split()))
insertion_sort(A, N)