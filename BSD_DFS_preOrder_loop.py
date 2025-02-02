# this code makes the tree that we'll traverse

class Node(object):

    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None

    # set value of the node
    def set_value(self,value):
        self.value = value

    # get value of the node
    def get_value(self):
        return self.value

    # set a node for the left child
    def set_left_child(self,left):
        self.left = left

    # set a node for the right child
    def set_right_child(self, right):
        self.right = right

    # get the node of left child
    def get_left_child(self):
        return self.left

    # get the node of right child
    def get_right_child(self):
        return self.right

    # check if node has left child -> return boolean
    def has_left_child(self):
        return self.left != None

    # check if node has right child -> return boolean
    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


# Let's define a stack to help keep track of the tree nodes
class Stack():
    def __init__(self):
        self.list = list()

    # add an element to the list
    def push(self,value):
        self.list.append(value)

    # remove the last element from the list
    def pop(self):
        return self.list.pop()

    # get the value of the last element in the list
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    # check if the list empty
    def is_empty(self):
        return len(self.list) == 0

    #
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s

        else:
            return "<stack is empty>"

class State(object):
  def __init__(self, node):
    self.node = node
    self.visited_left = False
    self.visited_right = False

  def get_node(self):
    return self.node
    
  def get_visited_left(self):
    return self.visited_left

  def get_visited_right(self):
    return self.visited_right

  def set_visited_right(self):
    self.visited_right = True

  def set_visited_left(self):
    self.visited_left = True

  def __repr__(self) -> str:
    s = f"""{self.node}
visited_left: {self.visited_left}
visited_right: {self.visited_right}
        """
    return s

def preorder_with_stack(node):
  visited_list = list()
  state = State(node)
  stack = Stack()
  stack.push(state)
  visited_list.append(node.get_value())
  while (node):
    if node.has_left_child() and not state.get_visited_left():
      state.set_visited_left()
      node = node.get_left_child()
      state = State(node)
      stack.push(state)
      visited_list.append(node.get_value())
    elif node.has_right_child() and not state.get_visited_right():
      state.set_visited_right()
      node = node.get_right_child()
      state = State(node)
      stack.push(state)
      visited_list.append(node.get_value())
    else:
      stack.pop()
      if stack.is_empty():
        node = None
      else:
        state = stack.top()
        node = state.get_node()
  return visited_list