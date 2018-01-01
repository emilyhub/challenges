# Finds the max of an array given a sliding window of size B
def slidingMaximum(A, B):
    window = []
    if B > len(A):
        return max(A)
    for i in range(0, B):
        window.append(A[i])
    B = []
    B.append(window[len(window) - 1])
    for i in range(1, len(A) - len(window) + 1):
        print("index ", i, " window: ", window)
        window = window[1:]
        window.append(A[i + len(window)])
        B.append(max(window))
    return B


print (slidingMaximum([6, 1, 7, 12, 4, 15, 1, 0, 1], 3))
