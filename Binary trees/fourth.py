import numpy as np
from random import randint

class BinaryTree():
  def __init__(self, root):
      self.key = root
      self.left = None
      self.right = None

  
  def delete_elem_tree(self, tree, elem):
        del_elem = self.find( elem)
        if del_elem is None:
            return None
        elif del_elem.GetLeft() is None and del_elem.GetRight() is None:
            del_elem.SetVal(None)
            self.del_Nones()
        elif del_elem.GetLeft() is None:
            del_elem.key = del_elem.GetRight().GetRoot()
            del_elem.left = del_elem.GetRight().GetLeft()
            del_elem.right = del_elem.GetRight().GetRight()
        elif del_elem.GetRight() is None:
            del_elem.key = del_elem.GetLeft().GetRoot()
            del_elem.right = del_elem.GetLeft().GetRight()
            del_elem.left = del_elem.GetLeft().GetLeft()
        else:
            right_elem = del_elem.GetRight()
            max_left = None
            while True:
                if right_elem.GetLeft() is None:
                    if max_left is None:
                        max_left = right_elem
                    del_elem.key = max_left.GetRoot()
                    self.delete_elem_tree(right_elem, max_left.GetRoot()) # 1 arg = right_elem
                    break
                else:
                    max_left =self.GetRight()
  def del_Nones(self):
          if not self.GetLeft() is None and self.GetLeft().GetRight() is None:
              self.left = None
          if not self.GetRight() is None and self.GetRight().GetRoot() is None:
              self.right = None
          if not self.GetLeft() is None:
              self.GetLeft().del_Nones()
          if not self.GetRight() is None:
              self.GetRight().del_Nones()


  def find(self, elem):
    if elem == int(self.GetRoot()):
      return self
    if self.GetLeft() is not None and self.GetRight().GetRoot() > elem:
      return self.GetLeft().find(elem)
    elif self.GetRight() is not None and self.GetRight().GetRoot() <= elem:
      return self.GetRight().find(elem)
    return None

  def insert_left(self, new_node=None):
      if self.left is None:
          self.left = BinaryTree(new_node)
      else:
          t = BinaryTree(new_node)
          t.left = self.left
          self.left = t

  def insert_right(self, new_node=None):
      if self.right is None:
          self.right = BinaryTree(new_node)
      else:
          t = BinaryTree(new_node)
          t.right = self.right
          self.right = t

  def GetRight(self):
      return self.right

  def GetLeft(self):
      return self.left

  def SetVal(self, obj):
      self.key = obj

  def GetRoot(self):
      return self.key

  def Spec_Insert(self,value):
    if self.GetRoot() is None:
      self.SetVal(value)
    
    elif self.GetRoot() <= value:
      if self.GetRight() is None:
        self.insert_right(value)
      else:
        self.GetRight().Spec_Insert(value)
    
    elif self.GetRoot() > value:
      if self.GetLeft() is None:
        self.insert_left(value)
      else:
        self.GetLeft().Spec_Insert(value)


def printTree(start,traver):
  if start:
    traver = traver + (str(start.key))+"-"
    traver= printTree(start.left, traver)
    traver = printTree(start.right,traver)
  return traver
  def Spec_Insert(self,value):
    if self.GetRoot() is None:
      self.SetVal(value)
  
tree=BinaryTree(1)  
lis=np.array([21,7,32,27,25,24,30,37,34,33,39,44,2,4,6,5,14,12,9,18])
for i in range (len(lis)):
  tree.Spec_Insert(lis[i])

a=printTree(tree,"")
print (a)
tree.delete_elem_tree(tree,39)
a=printTree(tree,"")
print (a)


  
