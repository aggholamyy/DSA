"""
The following function is not the correct solution for traversing a BST,
but it is the first recursive function I wrote that handled a specific test.
The main problem here is that this code traverses the whole tree using two separate recursive calls,
which causes it to miss many right children.
I want to keep this to track the evolution process of my solution.
"""

def pre_order(tree):
    root = tree.get_root()
    node = root
    visited_list = list()
    def travers_left(node, visited_list):
        if node is None:
            return visited_list
        else:
            visited_list.append(node)
            node = node.get_left_child()
            travers_left(node, visited_list)
    def travers_right(node, visited_list):
        if node is None:
            return visited_list
        else:
            node = node.get_right_child()
            if node:
                visited_list.append(node)
            travers_right(node, visited_list)
  
    travers_left(root, visited_list)
    travers_right(root, visited_list)
    return visited_list