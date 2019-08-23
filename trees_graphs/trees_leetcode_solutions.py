from trees_graphs.BinarySearchTree import BinarySearchTree
from trees_graphs.BinaryTree import BinaryTree
from trees_graphs.Codec import Codec
from trees_graphs.Node import Node
from trees_graphs.Node import NodeBinaryTree
from trees_graphs.Traversal import Traversal

class Solution(object):
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    ###################################################################################################################
    ###################################################################################################################
    ############################################ MAXIMUM DEPTH BINARY TREE 104 ########################################
    ###################################################################################################################
    ###################################################################################################################
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    ###################################################################################################################
    ###################################################################################################################
    ############################################ IS SAME TREE 100 #####################################################
    ###################################################################################################################
    ###################################################################################################################
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    ###################################################################################################################
    ###################################################################################################################
    ############################################ INVERT TREE 226 ######################################################
    ###################################################################################################################
    ###################################################################################################################
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        queue = [root]

        while queue:
            node = queue[0]
            queue.pop(0)
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left is not None: queue.append(node.left)
            if node.right is not None: queue.append(node.right)

        return root

    ###################################################################################################################
    ###################################################################################################################
    ############################################ LOWEST COMMON ANCESTOR 235 ###########################################
    ###################################################################################################################
    ###################################################################################################################
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root
        return None

    ###################################################################################################################
    ###################################################################################################################
    ############################################ SUBTREE OF ANOTHER TREE 572 ##########################################
    ###################################################################################################################
    ###################################################################################################################
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        queue = [s]
        while queue:
            n = queue[0]
            queue.pop(0)
            if n.val == t.val and self.isSameTree(n, t):
                return True
            else:
                if n.left is not None:
                    queue.append(n.left)
                if n.right is not None:
                    queue.append(n.right)
        return False

    ###################################################################################################################
    ###################################################################################################################
    ####################################### BINARY TREE LEVEL ORDER TRAVERSAL 102 #####################################
    ###################################################################################################################
    ###################################################################################################################
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans, level_nodes = [], [root]
        while root and level_nodes:
            ans.append([n.val for n in level_nodes])
            child_pairs = [[node.left, node.right] for node in level_nodes]
            level_nodes = [child for pair in child_pairs for child in pair if child]
        return ans

if __name__ == "__main__":
    ###################################################################################################################
    ###################################################################################################################
    ############################################ MAXIMUM DEPTH BINARY TREE 104 ########################################
    ###################################################################################################################
    ###################################################################################################################
    s = Solution()
    # [3,9,20,null,null,15,7]
    n1 = NodeBinaryTree(3)
    n2 = NodeBinaryTree(9)
    n3 = NodeBinaryTree(20)
    n4 = NodeBinaryTree(None)
    n5 = NodeBinaryTree(None)
    n6 = NodeBinaryTree(15)
    n7 = NodeBinaryTree(7)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    print(s.maxDepth(n1))

    ###################################################################################################################
    ###################################################################################################################
    ############################################ IS SAME TREE 100 #####################################################
    ###################################################################################################################
    ###################################################################################################################
    n_100_1 = NodeBinaryTree(3)
    n_100_2 = NodeBinaryTree(4)
    n_100_3 = NodeBinaryTree(5)
    n_100_4 = NodeBinaryTree(1)
    n_100_5 = NodeBinaryTree(2)
    n_100_1.left = n_100_2
    n_100_1.right = n_100_3
    n_100_2.left = n_100_4
    n_100_2.right = n_100_5

    n_100_a = NodeBinaryTree(4)
    n_100_b = NodeBinaryTree(1)
    n_100_c = NodeBinaryTree(2)
    n_100_a.left = n_100_b
    n_100_a.right = n_100_c
    print(s.isSameTree(n_100_2, n_100_a))

    ###################################################################################################################
    ###################################################################################################################
    ############################################ LOWEST COMMON ANCESTOR 235 ###########################################
    ###################################################################################################################
    ###################################################################################################################

    ###################################################################################################################
    ###################################################################################################################
    ############################################ SUBTREE OF ANOTHER TREE 572 ##########################################
    ###################################################################################################################
    ###################################################################################################################
    print(s.isSubtree(n_100_1, n_100_a))

    ###################################################################################################################
    ###################################################################################################################
    ####################################### BINARY TREE LEVEL ORDER TRAVERSAL 102 #####################################
    ###################################################################################################################
    ###################################################################################################################
    n3 = NodeBinaryTree(3)
    n9 = NodeBinaryTree(9)
    n20 = NodeBinaryTree(20)
    n15 = NodeBinaryTree(15)
    n7 = NodeBinaryTree(7)
    n3.left = n9
    n3.right = n20
    n20.left = n15
    n20.right = n7
    print(s.levelOrder(n3))