# Find the largest sum of any sized subarray of A

# maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
# 6 //subarray = [4, -1, 2, 1]

def maxSubArray(A):
    return helper(A[1:], [A[0]])

def helper(A, solution):
    if len(A) == 0:
        return solution
    print(solution)
    print(A[0] + sum(solution))
    if (A[0] > A[0] + sum(solution)):
        return helper(A[1:], A[0])
    else:
        return helper(A[1:], solution)

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
