import unittest
# Paths with sum
"""You are given a binary tree in which each node contains an integer value (pos or neg)
. Design algorithm to count number of paths that sum to a given value. The path does not need to start or 
end at the root or a leaf. But must go downwards Parent to child"""


class BinaryTree(object):
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


    def __repr__(self):
        return'<BinaryTreeNode {data}>'.format(data = self.data)


tree=BinaryTree(1,
        BinaryTree(2,
            BinaryTree(6,BinaryTree(10),BinaryTree(5)),
            BinaryTree(7)),
        BinaryTree(10,
            BinaryTree(8, BinaryTree(-1),BinaryTree(-5)),
            BinaryTree(-1, BinaryTree(2),BinaryTree(9))
            )
        )


def path(tree, val=19, sum_path=0):
    """returns number of all paths that sum upto given value"""

    # DFS and preOrder traversal

    # sum_path = sum_path + node.data

    # if sum_path equal val
        # count = count + 1

    # count += path(node.left, val, sum_path)
    # count+= path(node.right, val, sum_path)

    # return count


######################################
    
    if tree == None:
        return 0

    sum_path = sum_path + tree.data

    count = 0

    if sum_path == val:
        count += 1

    count += path(tree.left, val, sum_path)
    count += path(tree.right, val, sum_path)
    print('count--->', count)
    return count



print(path(tree))



class TestFunc(unittest.TestCase):
    def test_method(self):
        self.assertEqual(path(tree), 3)

if __name__ == "__main__":
    unittest.main(verbosity = 2)
