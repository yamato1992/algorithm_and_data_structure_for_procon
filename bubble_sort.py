def bubble_sort(A, N):
    flag = 1
    while flag:
        flag = 0
        for j in range(N - 1, 0, -1):
            if A[j] < A[j - 1]:
                A[j], A[j -1] = A[j - 1], A[j]
                flag = 1
                print(A)

N = int(input())
A = list(map(int, input().split()))
bubble_sort(A, N)
