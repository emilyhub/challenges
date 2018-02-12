# returns all pairs in arr that add up to goal; can detect duplicate elements
def twoSum(arr, goal):
    complement = set()
    solution = []
    for element in arr:
        if element in complement:
            solution.append([element, goal - element])
        complement.add(goal - element)
    return solution
