from random import randint

class Node(object):
  def __repr__(self):
    return f"Это объект с ключом {self.root}"
  def __init__ (self,root):
    self.root=root
    self.left=None
    self.right=None


def printTree(start,traver):
  if start:
    traver = traver + (str(start.root))+"- "
    traver= printTree(start.left, traver)
    traver = printTree(start.right,traver)
  return traver


class Binary_Tree(object):

  def __init__ (self, root):
    self.root=Node(root)
    
  def option (self, item):
    if item=="1":
      return self.TreePrint(tree.root)

    elif item=="2":
      return self.TaskTwo(tree.root)

    elif item=="3":
      return self.TaskThree(tree.root, 0)
    
    elif item=="4":
      return self.TaskFour(tree.root)

    elif item=="5":
      return self.TaskFive(tree.root)

  
  def TaskFive(self,start):
    if start:
      if not start.right is None and start.right.root=="5" :
        ka=int(start.right.root)
        ba=int(start.left.root)
        ka=ka-ba
        a=tree.root.left.root
        b=tree.root.right.right.root
        pu=a*ka/b
        print (pu)
      else :
        self.TaskFive(start.left)
        self.TaskFive(start.right)


  def TaskFour(self,start):
    if start:
      pic=start.right.right.root
      dic=int(start.right.left.root)
      click=start.left.root
      ob=click*pic+dic
      print (ob)
      

  def TaskThree(self,start, su):
    if start:
      if not start.right is None and start.right.root=="*" :
        hook=start.right
        if hook.right.root=="-":
          hook=hook.right
          a=int(hook.right.root)
          b=int(hook.left.root)
          su=a-b
          tree.root.right.right=Node(su)
          return self.TaskThree(start.left,su)
      
      elif start.left.root=="+":
        hook=start.left
        a=int(hook.left.root)
        b=int(hook.right.root)
        kar=a+b
        tree.root.left=Node(kar)
        pan=su*kar
        print (pan)
      








  def TaskTwo(self,start):
    if start:
      if start.right.root=="*":
        hook=start.right
        c=int(hook.right.root)
      if start.left.root=="+":
        hook=start.left
        a=int(hook.left.root)
        b=int(hook.right.root)
        su=(a+b)*c
        print (su)
      else:
        self.TaskTwo(start.left)
        self.TaskTwo(start.right)



  def TreePrint(self,start):
    if start:
      if start.left.root=="+":
        hook=start.left
        a=int(hook.left.root)
        b=int(hook.right.root)
        su=a+b
        print (su)
      elif start.right.root=="+":
        hook=start.right
        a=int(hook.right.root)
        b=int(hook.right.right)
        su=a+b
        print (su)
      else:
        self.TreePrint(start.left)
        self.TreePrint(start.right)
      

        




tree=Binary_Tree(1)
tree.root.left=Node("+")
tree.root.left.left=Node("2")
tree.root.left.right=Node("2")
a=printTree(tree.root,"")
print(a)
tree.option("1")

tree.root.left.right=Node("2")
tree.root.left.left=Node("3")
tree.root.right=Node("*")
tree.root.right.right=Node("4")
a=printTree(tree.root,"")
print(a)
tree.option("2")
tree.root.left=Node("lia")

tree.root.left.left=Node("+")
tree.root.left.left.left=Node("7")
tree.root.left.left.right=Node("8")
tree.root.right=Node("*")
tree.root.right.right=Node("-")
tree.root.right.right.right=Node("2")
tree.root.right.right.left=Node("1")
a=printTree(tree.root,"")
print(a)
tree.option("3")

tree.root.right.left=Node("7")
a=printTree(tree.root,"")
print(a)
tree.option("4")
tree.root.right.right.right=Node("5")
tree.root.right.right.left=Node("2")
a=printTree(tree.root,"")
print(a)
tree.option("5")



#alternative 
#from binarytree import Node


#root = Node(1)
#root.left = Node(2)
#root.right = Node(3)
#root.left.left = Node(4)
#root.left.right = Node(5)
#print(root)



class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def __repr__(self):
        return '{} [{}, {}]'.format(self.getRootVal(), self.getLeftChild(), self.getRightChild())


tree = BinaryTree('+')
tree.insertLeft(2)
tree.insertRight(2)
print(tree)

tree_1 = BinaryTree("*")
# tree_1.insertLeft(tree)
tree_1.insertLeft('+')
tree_1.getLeftChild().insertLeft(2)
tree_1.getLeftChild().insertRight(2)
tree_1.insertRight(4)
print(tree_1)


tree_2 = BinaryTree("*")
tree_2.insertLeft('-')
tree_2.insertRight('+')
tree_2.getLeftChild().insertLeft('7')
tree_2.getLeftChild().insertRight('8')
tree_2.getRightChild().insertLeft('2')
tree_2.getRightChild().insertRight('1')
print(tree_2)

tree_3 = BinaryTree("+")
# tree_3.insertLeft(tree_2)
tree_3.insertLeft("*")
tree_3.getLeftChild().insertLeft('-')
tree_3.getLeftChild().insertRight('+')
tree_3.getLeftChild().getLeftChild().insertLeft('7')
tree_3.getLeftChild().getLeftChild().insertRight('8')
tree_3.getLeftChild().getRightChild().insertLeft('2')
tree_3.getLeftChild().getRightChild().insertRight('1')
tree_3.insertRight('7')
print(tree_3)

tree_2 = BinaryTree("/")
tree_2.insertLeft('*')
tree_2.insertRight('-')
tree_2.getRightChild().insertLeft('2')
tree_2.getRightChild().insertRight('1')
tree_2.getLeftChild().insertLeft('+')
tree_2.getLeftChild().insertRight('-')
tree_2.getLeftChild().getLeftChild().insertLeft('7')
tree_2.getLeftChild().getLeftChild().insertRight('8')
tree_2.getLeftChild().getRightChild().insertLeft('5')
tree_2.getLeftChild().getRightChild().insertRight('2')
print(tree_2)
