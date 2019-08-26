from trees_graphs.Traversal import Traversal
from trees_graphs.Node import NodeBinaryTree

class BinarySearchTree(object):
    def __init__(self, list):
        list.sort()
        def createBST(list):
            if not list:
                return None
            mid = int(len(list)/2)
            root = NodeBinaryTree(list[mid])
            root.left = createBST(list[:mid])
            root.right = createBST(list[mid+1:])
            return root
        self.root = createBST(list)

    ###################################################################################################################
    ###################################################################################################################
    ################################ IS VALID BST? 98 #################################################################
    ###################################################################################################################
    ###################################################################################################################
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        BSTs' inorder traversal is always in increasing order
        """
        if root is None: return True
        t = Traversal()
        l = t.inorder_traversal(root)
        for n in range(0, len(l)-1):
            if l[n] > l[n+1]:
                return False
        return True

    ###################################################################################################################
    ###################################################################################################################
    ################################ KTHSMALLEST 230 ##################################################################
    ###################################################################################################################
    ###################################################################################################################
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        t = Traversal()
        l = t.inorder_traversal(root)
        return l[k]

if __name__ == '__main__':
    ###################################################################################################################
    ###################################################################################################################
    ################################ CREATE BST #######################################################################
    ###################################################################################################################
    ###################################################################################################################
    list = [1, 2, 3, 4, 5]
    bst = BinarySearchTree(list)
    t = Traversal()
    t.traverse(bst.root, 'inorder')
    ###################################################################################################################
    ###################################################################################################################
    ################################ IS VALID BST? 98 #################################################################
    ###################################################################################################################
    ###################################################################################################################

