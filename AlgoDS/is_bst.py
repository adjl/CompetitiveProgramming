"""
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""


def check_binary_search_tree_(root):
    is_bst, _ = _check_binary_search_tree_(root)
    return is_bst


def _check_binary_search_tree_(root):
    if root is None:
        return (True, None)
    is_left_bst, left = _check_binary_search_tree_(root.left)
    is_right_bst, right = _check_binary_search_tree_(root.right)
    if is_left_bst and is_right_bst:
        if left and right:
            return (left.data < root.data < right.data, root)
        elif left:
            return (left.data < root.data, root)
        elif right:
            return (root.data < right.data, root)
        return (True, root)
    return (False, None)
