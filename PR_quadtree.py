from Leaf import Leaf


class PR_quadtree:


    def __init__(self):
        self.root = Leaf(2**16, 2**16)  #we start the tree with a root node with value (N,N), and it has 4 leaves

    def insert(self, leaf, N=2**16):
        self.root = self.insert_recursive(self.root, leaf, N / 2, N / 2, 2)

    def insert_recursive(self, root, leaf, x, y, div, N=2**16):
        if root is None:
            return leaf

        else:
            if root.is_leaf() and root != self.root:    #if node isn't null and is leaf, pass the value to a sub-leaf
                root.expand_leaf(x, y)

            if leaf.x < x and leaf.y < y:
                x -= N / (2 ** div)
                y -= N / (2 ** div)
                div += 1
                root.nw = self.insert_recursive(root.nw, leaf, x, y, div)   #go to north-west node

            elif leaf.x < x and leaf.y >= y:
                x -= N / (2 ** div)
                y += N / (2 ** div)
                div += 1
                root.sw = self.insert_recursive(root.sw, leaf, x, y, div)   #go to south-west node

            elif leaf.x >= x and leaf.y < y:
                x += N / (2 ** div)
                y -= N / (2 ** div)
                div += 1
                root.ne = self.insert_recursive(root.ne, leaf, x, y, div)   #go to north-east node

            elif leaf.x >= x and leaf.y >= y:
                x += N / (2 ** div)
                y += N / (2 ** div)
                div += 1
                root.se = self.insert_recursive(root.se, leaf, x, y, div)   #go to south-east node

            return root

    def search(self, leaf, N=2**16):
        depth = self.depth_search(self.root, leaf, N / 2, N / 2, 2, 0)
        return depth

    def depth_search(self, root, leaf, x, y, div, level, N=2**16):
        if root is None:
            return level - 1

        elif root.is_leaf():
            if root.x == leaf.x and root.y == leaf.y:
                return level

        else:

            level += 1

            if leaf.x < x and leaf.y < y:
                x -= int(N / (2 ** div))
                y -= int(N / (2 ** div))
                div += 1
                return self.depth_search(root.nw, leaf, x, y, div,level)

            elif leaf.x < x and leaf.y >= y:
                x -= N / (2 ** div)
                y += N / (2 ** div)
                div += 1
                return self.depth_search(root.sw, leaf, x, y, div,level)

            elif leaf.x >= x and leaf.y < y:
                x += N / (2 ** div)
                y -= N / (2 ** div)
                div += 1
                return self.depth_search(root.ne, leaf, x, y, div,level)

            elif leaf.x >= x and leaf.y >= y:
                x += N / (2 ** div)
                y += N / (2 ** div)
                div += 1
                return self.depth_search(root.se, leaf, x, y, div,level)

        return level
