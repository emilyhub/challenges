# given a BST, returns whether tree is balanced
def balanced(root):
    def help(root):
        if root is None:
            return -1
        lefty = help(root.left)
        righty = help(root.right)
        if lefty == -1 or righty == -1 or Math.abs(lefty - righty) > 1:
            return -1
        return 1 + max(lefty, righty)
    return help(root) != -1
