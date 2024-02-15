# username - eithankatz
# id1      - 212937817
# name1    - Ohad Sapir
# id2      - 213452311
# name2    - Eithan Katz


"""A class representing a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.
    if given not value parameter, create virtual node

    @type value: str
    @param value: data of your node
    """

    def __init__(self, value=None):
        self.value = value
        self.parent = None
        if value is None:
            self.left = None
            self.right = None
            self.height = -1
            self.size = 0
        else:
            self.left = AVLNode()
            self.right = AVLNode()
            self.height = 0
            self.size = 1

    """returns the left child

	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""

    def getLeft(self):
        return self.left

    """returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""

    def getRight(self):
        return self.right

    """returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""

    def getParent(self):
        return self.parent

    """return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""

    def getValue(self):
        return self.value

    """returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""

    def getHeight(self):
        return self.height

    """returns the balance factor

	@rtype: int
	@returns: the balance factor of self
	"""

    def getBalance(self):
        bf = 0
        bf += self.left.height
        bf -= self.right.height
        return bf

    """returns the size

	@rtype: int
	@returns: the size of self, 0 if the node is virtual
	"""

    def getSize(self):
        return self.size

    """sets left child

	@type node: AVLNode
	@param node: a node
	"""

    def setLeft(self, node):
        node.left = AVLNode()
        node.right = AVLNode()
        self.left = node

    """sets right child

	@type node: AVLNode
	@param node: a node
	"""

    def setRight(self, node):
        node.left = AVLNode()
        node.right = AVLNode()
        self.right = node

    """sets parent

	@type node: AVLNode
	@param node: a node
	"""

    def setParent(self, node):
        self.parent = node

    """sets value

	@type value: str
	@param value: data
	"""

    def setValue(self, value):
        self.value = value

    """sets the height of the node

	@type h: int
	@param h: the height
	"""

    def setHeight(self, h):
        self.height = h

    """sets the size of the node

	@type s: int
	@param s: the size
	"""

    def setSize(self, s):
        self.size = s

    """returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""

    def isRealNode(self):
        return self.getHeight() != -1

    """returns whether self has a left son

	@rtype: bool
	@returns: True if self has left son, False otherwise.
	"""

    def hasLeft(self):
        if self.left is None:
            return False
        else:
            return self.left.isRealNode()

    """returns whether self has a right son

	@rtype: bool
	@returns: True if self has right son, False otherwise.
	"""

    def hasRight(self):
        if self.right is None:
            return False
        else:
            return self.right.isRealNode()

    """returns whether self has only one child

	@rtype: bool
	@returns: True if self has exactly one son, False otherwise.
	"""

    def hasOneChild(self):
        return (self.hasRight() and not self.hasLeft()) or (self.hasLeft() and not self.hasRight())

    """returns the only child of self

	@pre: self has only one child
	@rtype: AVLNode
	@returns: Left child if self has only left child, right child if self has only right child
	"""

    def getOnlyChild(self):
        if self.hasLeft():
            return self.left
        elif self.hasRight():
            return self.right

    """returns whether self is a leaf

	@rtype: bool
	@returns: True if self is a leaf, False otherwise.
	"""

    def isLeaf(self):
        if self.isRealNode():
            return (not self.left.isRealNode()) and (not self.right.isRealNode())

    """returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""

    def listToArrayRec(self, arr):
        if self.isRealNode():
            if self.hasLeft():      # left part of the list first
                self.getLeft().listToArrayRec(arr)
            arr.append(self.value)  # add current item
            if self.hasRight():     # then add right part of the list
                self.getRight().listToArrayRec(arr)
        return arr

    """searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""

    def searchRec(self, val, i):
        left = self.left
        right = self.right

        if self.value == val:
            return i

        if self.hasLeft():
            x = left.searchRec(val, i - left.right.size - 1)
        else:
            x = -1

        if self.hasRight():
            y = right.searchRec(val, i + right.left.size + 1)
        else:
            y = -1

        return max(x, y)

    """returns whether the node is a left child or a right child

	@rtype: boolean
	@returns: True if self is a left child of it's parent, False otherwise.
	"""

    def isLeftChild(self):
        return self is self.getParent().getLeft()

    """updates the height of the node based on its children's height

	@rtype: int
	@returns: 1 if the height was changed, 0 otherwise
	"""

    def updateHeight(self):
        prevHeight = self.height
        self.setHeight(1 + max(self.getLeft().getHeight(), self.getRight().getHeight()))
        if self.height != prevHeight:
            return 1
        else:
            return 0

    """updates the size of the node  based on its children's size"""

    def updateSize(self):
        self.size = 1 + self.left.size + self.right.size

    """gets the successor node of self

	@rtype: AVLNode
	@returns: the successor of self. The next item in list. 
	if self is last and has no successor, returns self
	"""

    def successor(self):
        cur = self
        # if has right, than go right once and then left all the way
        if self.hasRight():
            cur = self.right
            while cur.hasLeft():
                cur = cur.left
            return cur
        # otherwise, go up-left until going up-right
        else:
            y = self.parent
            while y.isRealNode() and cur == y.right:
                cur = y
                y = cur.parent
            return y

    """gets the predecessor node of self

	rtype: AVLNode
	@returns: the predecessor of self. The previous item in list.
	if self is first and has no predecessor, returns self
	"""

    def predecessor(self):
        cur = self
        # if has left, go left once and then right all thee way
        if self.hasLeft():
            cur = self.left
            while cur.hasRight():
                cur = cur.right
            return cur
        # otherwise, go up-right until going up-left
        else:
            y = self.parent
            while y.isRealNode() and cur == y.left:
                cur = y
                y = cur.parent

            return y

    """deletes the given leaf from the list

	@pre: self.isLeaf()
	"""

    def deleteLeaf(self):
        if self.isLeftChild():
            self.parent.left = AVLNode()
        else:
            self.parent.right = AVLNode()

    """joining self with x and lst ---> [self, x, lst]

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after x
	@type x: AVLNode
	@pre: x is not None
	@param lst: a node to be concatenated between self and lst 
	@rtype: AVLTreeList
	@returns: the root joined list
	"""

    def join(self, xVal, lst):
        # Creating new lists with self and lst as their roots and joining both lists
        lst1 = AVLTreeList()
        lst1.root = self
        lst2 = AVLTreeList()
        lst2.root = lst
        return lst1.join(xVal, lst2)


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root = AVLNode()
        self.firstItem = None
        self.lastItem = None

    # add your fields here

    def getTreeHeight(self):
        return self.root.height

    """returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""

    def empty(self):
        return not self.root.isRealNode()

    def select(self, i):
        cur = self.root
        if i > cur.size:
            return -1
        else:
            while cur.isRealNode():
                r = cur.left.size + 1
                # Case 1: Item found
                if r == i:
                    return cur
                # Case 2: Item is on the left
                elif r > i:
                    cur = cur.left
                # Case 3: Item on the right
                elif r < i:
                    i -= r
                    cur = cur.right

    """retrieves the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the i'th item in the list
	"""

    def retrieveNode(self, i):
        return self.select(i + 1)

    """retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the value of the i'th item in the list
	"""

    def retrieve(self, i):
        if i < 0 or i >= self.length():
            return None
        else:
            return self.retrieveNode(i).getValue()

    """update first and last fields by retrieving first and last items"""

    def updateFirstLast(self):
        if self.empty():
            self.firstItem = None
            self.lastItem = None
        else:
            self.firstItem = self.retrieveNode(0)
            self.lastItem = self.retrieveNode(self.length() - 1)

    """inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def insert(self, i, val):
        # Insert first node to empty list
        if i == 0 and self.empty():
            self.root = AVLNode(val)
            self.firstItem = self.root
            self.lastItem = self.root
            return 0
        # Insert after last node
        elif i == self.root.size:
            # inserting new item as the new last item and rebalancing
            nodeLast = self.lastItem
            nodeLast.right = AVLNode(val)
            nodeLast.right.parent = nodeLast
            self.lastItem = nodeLast.right
            cnt = self.insertRebalance(nodeLast)
        # Insert at the middle of list
        else:
            z = AVLNode(val)
            if i == 0:
                self.firstItem = z      # update firstItem field if necessary
            nodeI = self.retrieveNode(i)

            # Find predecessor (down-left) and insert new node as its right child (predecessor must be leaf)
            if nodeI.hasLeft():
                pred = nodeI.predecessor()
                pred.right = z
                z.parent = pred
                pred.updateHeight()
                cnt = self.insertRebalance(pred)
            # If possible, insert new node as the left child (and thus predecessor) of current i'th item
            else:
                nodeI.left = z
                z.parent = nodeI
                nodeI.updateHeight()
                cnt = self.insertRebalance(nodeI)
        return cnt

    """insert val as the last item in list"""

    def append(self, val):
        return self.insert(self.length(), val)

    '''	Balance the tree by promoting and rotating.

    Balance bottom-up and re-calculate sizes as we go up the branch.
	@param: node The AVLNode from which to start balancing up until root.
	@return: number of rebalancing operations needed
	'''

    def insertRebalance(self, node):
        if node is None:
            return 0
        cnt = 0
        cur = node
        while cur is not None:
            # What is the criminal BF? - right son
            if cur.getBalance() == -2:
                # Left rotation
                if cur.right.getBalance() == -1:
                    cnt += self.rotateLeft(cur)
                # Right then left rotation
                elif cur.right.getBalance() == 1:
                    cnt += self.rotateRight(cur.right)
                    cnt += self.rotateLeft(cur)
                # Special case only use in join function
                elif cur.right.getBalance() == 0:
                    cnt += self.rotateLeft(cur)

            # What is the criminal BF? - left son
            if cur.getBalance() == 2:
                # Right rotation
                if cur.left.getBalance() == 1:
                    cnt += self.rotateRight(cur)
                # Right then left rotation
                elif cur.left.getBalance() == -1:
                    cnt += self.rotateLeft(cur.left)
                    cnt += self.rotateRight(cur)
                # Special case only use in join function
                elif cur.left.getBalance() == 0:
                    cnt += self.rotateRight(cur)
            # BF is legal, keep updating size and height until the root
            else:
                cnt += cur.updateHeight()
            if cur.hasLeft():
                cur.left.updateHeight()
            if cur.hasRight():
                cur.right.updateHeight()
            cur.updateHeight()
            cur.updateSize()
            cur = cur.parent
        return cnt

    '''
	Rotate right on the given node.
	Rotate on node >y< will produce the following:
				 y                 x
		  ______/ \__    =>     __/ \______
		 x           c   =>    a           y
	  __/ \__            =>             __/ \__
	 a       b                         b       c

	@rtype: int
	@return: 1
	@param node Node to be rotated
	'''

    def rotateRight(self, y):
        x = y.left
        b = x.right

        # modify root
        if y.parent is None:
            self.root = x
        elif y.isLeftChild():
            y.parent.left = x
        else:
            y.parent.right = x

        # Update parents
        x.parent = y.parent
        b.parent = y
        y.parent = x

        # rotate
        y.left = b
        x.right = y

        # update sub-tree sizes
        y.updateSize()
        x.updateSize()
        return 1

    '''
	Rotate left on the given node.
	Rotate on node >x< will produce the following:
		 x                              y
	  __/ \______       =>       ______/ \__
	 a           y      =>      x           c
			  __/ \__   =>   __/ \__
			 b       c      a       b

	@rtype: int
	@return: 1
	@param node Node to be rotated
	'''

    def rotateLeft(self, x):
        y = x.right
        b = y.left

        # modify root
        if x.parent is None:
            self.root = y
        elif x.isLeftChild():
            x.parent.left = y
        else:
            x.parent.right = y

        # Update parents
        y.parent = x.parent
        b.parent = x
        x.parent = y

        # rotate
        x.right = b
        y.left = x

        # update sub-tree sizes
        x.updateSize()
        y.updateSize()
        return 1

    """deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operations needed
	"""

    def delete(self, i):
        # out of boundaries
        if i < 0 or i >= self.length():
            return -1
        else:
            del_node = self.retrieveNode(i)
            parent = del_node.parent

            # Case 1: Node has both left and right children
            if del_node.hasLeft() and del_node.hasRight():
                # Replace node with its successor until leaf or one child
                while del_node.hasLeft() and del_node.hasRight():
                    succ = del_node.successor()
                    parent = succ.parent
                    del_node.value = succ.value
                    del_node = succ

            # Case 2: Node is leaf - simply delete and update root if necessary
            if del_node.isLeaf():
                if del_node is self.root:
                    self.root = AVLNode()
                else:
                    del_node.deleteLeaf()

            # Case 3: Node has single child
            # parent                              parent
            #       \__                   =>            \__
            #           node              =>              child
            #                \__          =>
            #                   child
            elif del_node.hasOneChild():
                child = del_node.getOnlyChild()
                if del_node is self.root:
                    child.parent = None
                    self.root = child
                else:
                    child.parent = del_node.parent
                    if del_node.isLeftChild():
                        del_node.parent.left = child
                    else:
                        del_node.parent.right = child

            # Rebalance the tree and update firstItem and lastItem fields
            ret = self.deleteRebalance(parent)
            self.updateFirstLast()
            return ret

    """deletes the last item in the list and returns it

	@pre: list is not empty
	@rtype: AVLNode
	@returns: the removed Node
	"""

    def removeLast(self):
        if not self.empty():
            lastNode = self.lastItem
            ret = AVLNode()
            ret.value = lastNode.value
            self.deleteLast()
            return ret

    '''	Balance the tree by promoting and rotating.

	Balance bottom-up and re-calculate sizes as we go up the branch.
	@param: node The AVLNode from which to start balancing up until root.
	@return: number of rebalancing operations needed
	'''

    def deleteRebalance(self, node):
        if node is None:
            return 0
        cnt = 0
        cur = node
        cur.updateHeight()      # update height of initial insertion. Not counted as a balance operation
        while cur is not None:
            # What is the criminal BF? - right son
            if cur.getBalance() < -1:
                # Left rotation
                if cur.right.getBalance() <= 0:
                    cnt += self.rotateLeft(cur)
                # Right then left rotation
                else:
                    cnt += self.rotateRight(cur.right)
                    cnt += self.rotateLeft(cur)

            # What is the criminal BF? - left son
            if cur.getBalance() > 1:
                # Right rotation
                if cur.left.getBalance() >= 0:
                    cnt += self.rotateRight(cur)
                # Right then left rotation
                else:
                    cnt += self.rotateLeft(cur.left)
                    cnt += self.rotateRight(cur)

            if cur.hasLeft():
                cnt += cur.left.updateHeight()
                cur.left.updateSize()
            if cur.hasRight():
                cnt += cur.right.updateHeight()
                cur.right.updateSize()
            cnt += cur.updateHeight()
            cur.updateSize()
            cur = cur.parent
        return cnt

    """returns the value of the first item in the list

	@rtype: string
	@returns: the value of the first item, None if the list is empty
	"""

    def first(self):
        if self.empty():
            return None
        else:
            return self.firstItem.value

    """returns the value of the last item in the list

	@rtype: string
	@returns: the value of the last item, None if the list is empty
	"""

    def last(self):
        if self.empty():
            return None
        else:
            return self.lastItem.value

    """returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""

    def listToArray(self):
        arr = []
        return self.getRoot().listToArrayRec(arr)

    def deleteLast(self):
        if not self.empty():
            self.delete(self.length() - 1)

    """returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""

    def length(self):
        return self.root.getSize()

    """splits the list at the i'th index

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""

    def split(self, i):
        x = self.retrieveNode(i)
        leftTree = x.left
        rightTree = x.right
        return self.splitLoop(x, leftTree, rightTree)

    def splitLoop(self, x, leftTree, rightTree):
        cur = x
        while cur.parent is not None:
            parent = cur.parent
            # Going up-right
            if cur.isLeftChild():
                rightTree = rightTree.join(parent.value, parent.right)
            # Going up-left
            else:
                leftTree = parent.left.join(parent.value, leftTree)
            cur = parent
        # returning [leftTree, x, rightTree]
        leftTree.parent = None
        leftList = AVLTreeList()
        leftList.root = leftTree
        leftList.updateFirstLast()
        rightTree.parent = None
        rightList = AVLTreeList()
        rightList.root = rightTree
        rightList.updateFirstLast()
        return [leftList, x.value, rightList]

    """get the first left subtree of root that is of height <= h

	@type h: int
	@pre: 0 <= h < self.height()
	@param h: The intended maximal height of desired subtree
	@rtype: AVLNode
	@returns: the first left subtree of root that is of height <= h
	"""

    def getLeftSubtreeH(self, h):
        cur = self.root
        while cur.height > h and cur.left.isRealNode():
            cur = cur.left
        return cur

    """get the first right subtree of root that is of height <= h

	@type h: int
	@pre: 0 <= h < self.height()
	@param h: The intended maximal height of desired subtree
	@rtype: AVLNode
	@returns: the first right subtree of root that is of height <= h
	"""

    def getRightSubtreeH(self, h):
        cur = self.root
        while cur.height > h and cur.right.isRealNode():
            cur = cur.right
        return cur

    """concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""

    def concat(self, lst):
        diff = abs(self.getTreeHeight() - lst.getTreeHeight())      # get height differance
        # If lst is empty, nothing to concat
        if not lst.empty():
            # If self is empty, nothing to concat
            if self.empty():
                self.root = lst.root
            else:
                x = self.removeLast()
                self.join(x.value, lst)

        self.updateFirstLast()
        return diff

    """joining self with x and lst ---> [self, x, lst]

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after x
	@type x: AVLNode
	@pre: x is not None
	@param lst: a node to be concatenated between self and lst 
	@rtype: AVLTreeList
	@returns: the root joined list
	"""

    def join(self, xVal, lst):
        x = AVLNode(xVal)
        # Case 1: self is shorter
        #
        #                         /\
        #                        /  \
        #                       /    \
        #                      c      \
        #               _____ /  \     \
        #              x          \     \
        #       _____/   \_____    \     \
        #      /               \    \     \
        #    a                  b    \     \
        #   /  \   |       |   / \    \     \
        #  /self\  h       h  /   \    \     \
        # /______\ |       | /_____\    \_____\

        if self.getTreeHeight() <= lst.getTreeHeight():
            a = self.root
            b = lst.getLeftSubtreeH(self.getTreeHeight())
            c = b.parent
            if b is lst.root:
                self.root = x
            else:
                c.left = x
                x.parent = c
                self.root = lst.root
            self.root.parent = None

            a.parent = x
            x.left = a
            b.parent = x
            x.right = b

        # Case 2: lst is shorter
        #
        #            /\
        #           /  \
        #          /    \
        #         /      c
        #        /     /   \_____
        #       /     /          x
        #      /     /    _____/   \_____
        #     /     /    /               \
        #    /     /    b                 a
        #   /     /    / \   |       |   / \
        #  /     /    /   \  h       h  /lst\
        # /_____/    /_____\ |       | /_____\

        else:
            a = lst.root
            b = self.getRightSubtreeH(lst.getTreeHeight())
            c = b.parent

            if b is self.root:
                self.root = x
            else:
                c.right = x
                x.parent = c
            self.root.parent = None

            a.parent = x
            x.right = a
            b.parent = x
            x.left = b

        self.insertRebalance(x)
        self.updateFirstLast()
        return self.root

    """searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""

    def search(self, val):
        if self.empty():
            return -1
        return self.root.searchRec(val, self.root.left.size)

    """returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""

    def getRoot(self):
        return self.root


