# find two elements in arr that add to goal
def match(arr, goal):
    need = set()
    for element in arr:
        if element in need:
            return [element, goal - element]
        need.add(goal - element)
    return False