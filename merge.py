# merges two sorted arrays

def merge(arr1, arr2):
    pointer1, pointer2 = 0, 0
    solution = []
    while pointer1 < len(arr1) and pointer2 < len(arr2):
        if arr1[pointer1] < arr2[pointer2]:
            solution.append(arr1[pointer1])
            pointer1 += 1
        else:
            solution.append(arr2[pointer2])
            pointer2 += 1

    if pointer1 >= len(arr1):
        solution.append(arr2[pointer2:])
    if pointer2 >= len(arr2):
        solution.append(arr1[pointer1:])
    return solutions