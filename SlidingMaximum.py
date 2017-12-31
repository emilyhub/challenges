# Finds the max of an array given a sliding window of size B
def slidingMaximum(A, B):
    window = []
    if B > len(A):
        return max(A)
    for i in range(0, B):
        window.append(A[i])
    B = []
    B.append(max(window))
    for i in range(2, len(A) - len(window) + 2):
        window = window[1:]
        window.append(A[i])
        B.append(max(window))
    return B

print slidingMaximum([6, 1, 7, 12, 3, 6, 5, 8, 3, 4, 15, 1], 9)
