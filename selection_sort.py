def selection_sort(A, N):
    for i in range(N):
        min_index = i
        for j in range(i, N):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
        print(A)


N = int(input())
A = list(map(int, input().split()))
selection_sort(A, N)
