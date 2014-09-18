class tree_node(object):

    def __init__(value):
        value = value
        left_child = None
        right_child = None

class binary_tree(object):

    def __init__(value):
        root = tree_node(value)
        depth = 1

    def add(value):
        if root.left_child is None:
            left_child = tree_node(value)
        elif root.right_child is None:
            right_child = tree_node(value)

def random_tree_node(tree):
