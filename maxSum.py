# get max sum of contiguous subarray
def maxSum(arr):
    maxCurrent = maxGlobal = arr[0]
    for element in arr[1:]:
        maxCurrent = max(element, maxCurrent + element)
        if maxCurrent > maxGlobal:
            maxGlobal = maxCurrent
    return maxGlobal
