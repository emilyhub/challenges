# Takes an array A and returns the elements into a sequence such that
# a1 >= a2 <= a3 >= a4 <= a5... in lexicographical order
# if multiple solutions possible

def wave(A):
    A.sort()
    for i in range(0, len(A)):
        if i % 2 == 0 and i + 1 < len(A):
            A[i], A[i + 1] = A[i + 1], A[i]
    return A
print(wave([3, 1, 2, 4, 5]))
