"""
The following function is the correct solution for traversing a BST,
"""

def travers_preorder_bsd(root):
  visited_list = list()
  
  def traveler(node, visited_list):
    if node is None:
      return visited_list
    visited_list.append(node)
    traveler(node.get_left_child(), visited_list)
    traveler(node.get_right_child(), visited_list)
    return visited_list
  traveler(root, visited_list)
  return visited_list