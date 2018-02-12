# gets elements in arr that have occurred an odd number of times
def odd(arr):

    oddElements = set()
    answer = []
    for i in arr:
        if i in oddElements:
            oddElements.remove(i)
        else:
            oddElements.add(i)
    arr = [x for x in arr if x in oddElements]
    return arr
