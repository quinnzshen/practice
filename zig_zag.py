def zig_zag(tree):
    if tree.empty():
        return
    current_level = [tree.root()]
    next_level = []
    left_to_right = True

    while not current_level.empty():
        if left_to_right:
            current_node = current_level.dequeue()
            current_node.visit()
            if current_node.has_left_child():
                next_level.add(current_node.left_child())
            if current_node.has_right_child():
                next_level.add(current_node.right_child())
        else:
            current_node = current_level.pop()
            current_node.visit()
            if current_node.has_right_child():
                next_level.add(current_node.right_child())
            if current_node.has_left_child():
                next_level.add(current_node.left_child())
        if current_level.empty():
            current_level = next_level
            left_to_right = not left_to_right

