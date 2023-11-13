from Node import Node


class KD_tree:

    def __init__(self):
        self.root = None

    def insert(self, node):
        level = 0
        self.root = self.insert_recursive(self.root, node, level)

    def insert_recursive(self, root, node, level):
        if root is None:    # if the node we want to insert doesn't exist , add it to the tree
            return node

        elif level % 2 == 0:    # compare 'x' value
            level += 1
            if node.x < root.x:  # go to left node
                root.left = self.insert_recursive(root.left, node, level)
            else:                # go to right node
                root.right = self.insert_recursive(root.right, node, level)

        elif level % 2 == 1:    # compare 'y' value
            level += 1
            if node.y < root.y:  # go to left node
                root.left = self.insert_recursive(root.left, node, level)

            else:                # go to right node
                root.right = self.insert_recursive(root.right, node, level)
        return root

    def search(self, node):
        level = 0
        depth = self.depth_search(self.root, node, level)
        return depth

    def depth_search(self, root, node, level):
        if root is None:        # if the node we searched doesn't exist, we reached the end of the tree
            return level - 1    # return the correct depth of the tree

        elif root.x == node.x and root.y == node.y:  # if the pair found return the current level
            return level

        elif level % 2 == 0:    # compare 'x' value
            level += 1
            if node.x < root.x:
                return self.depth_search(root.left, node, level)

            else:
                return self.depth_search(root.right, node, level)

        elif level % 2 == 1:    # compare 'y' value
            level += 1
            if node.y < root.y:
                return self.depth_search(root.left, node, level)

            else:
                return self.depth_search(root.right, node, level)
        return level
