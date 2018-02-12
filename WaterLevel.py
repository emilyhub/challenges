def trap(A):
    i = 1
    water = 0
    while i < len(A) - 1:
        if A[i] < A[i - 1]:
            peak = -1
            for j in range(i + 1, len(A)):
                if A[j] >= A[j + 1]:
                    peak = j
                    break
            if peak != -1:
                for index in range(i, peak):
                    water += min(A[i - 1], A[peak]) - A[index]
                i = peak
        i += 1
        print("index ", i, " Water level ", water)
    return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
