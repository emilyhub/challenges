def trap(A):
    sdf
    water = 0
    for i in xrange(1, len(A) - 1):
        if A[i] < A[i - 1]:
            if A[i] < A[i + 1]:
                water += min(A[i - 1], A[i + 1])
                print("water level is now ", water)
            else:
                blockedIndex = -1
                for j in xrange(i + 2, len(A)):
                    if A[j] >= A[i]:
                        blockedIndex = j
                        break
                if blockedIndex != -1:
                    for index in xrange(i, blockedIndex):
                        water += A[i - 1] - A[index]
                        print("aggregating water for ", index, " level now ", water)
    return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
