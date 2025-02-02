"""
The following function is not the correct solution for traversing a BST,
but it is the first recursive function I wrote that handled a specific test.
The main problem here is that this code traverses the whole tree using two separate recursive calls,
which causes it to miss many right children.
I want to keep this to track the evolution process of my solution.
"""

def travers_preorder_bsd(node):
  visited_list = list()
#########################
# visited_list must be init by root
#  visited_list.append(node)
  #########################

  def traveler(node, visited_list):
    if node is None:
      return visited_list
    current_node = node
    visited_list.append(current_node)
    node = node.get_left_child()
    traveler(node, visited_list)
    node = current_node.get_right_child()
    traveler(node, visited_list)
    return visited_list
  traveler(root, visited_list)
  return visited_list