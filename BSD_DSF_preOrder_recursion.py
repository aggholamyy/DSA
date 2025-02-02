"""
The following function is not the correct solution for traversing a BST,
but it is the first recursive function I wrote that handled a specific test.
The main problem here is that this code traverses the whole tree using two separate recursive calls,
which causes it to miss many right children.
I want to keep this to track the evolution process of my solution.
"""

def travers_preorder_bsd(root):
  visited_list = list()
  
  def traveler(node, visited_list):
    if node is None:
      return visited_list
    current_node = node
    visited_list.append(current_node)
    traveler(node.get_left_child(), visited_list)
    traveler(current_node.get_right_child(), visited_list)
    return visited_list
  traveler(root, visited_list)
  return visited_list