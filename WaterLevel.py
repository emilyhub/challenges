def trap(A):
    i = 1
    water = 0
    while i < len(A) - 1:
        if A[i] < A[i - 1]:
            if A[i] < A[i + 1]:
                water += min(A[i - 1], A[i + 1]) - A[i]
            else:
                blockedIndex = -1
                for j in range(i + 2, len(A)):
                    if A[j] >= A[i - 1]:
                        blockedIndex = j
                        break
                if blockedIndex != -1:
                    for index in range(i, blockedIndex):
                        water += A[i - 1] - A[index]
                    i += blockedIndex - i
        i += 1
    return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
