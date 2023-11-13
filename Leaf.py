class Leaf:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nw = self.sw = self.ne = self.se = None

    def is_leaf(self):  # check if the object is leaf or pointer to other leaves
        if self.nw == self.sw == self.ne == self.se == None:
            return True
        else:
            return False

    # parameters x,y are the center of the leaf and divide the leaf to four equal areas
    def expand_leaf(self, x, y):    # current object becomes pointer to other leaves so the values x,y are assigned to a sub-leaf
        if self.x < x and self.y < y:       # north-west
            self.nw = Leaf(self.x, self.y)

        elif self.x < x and self.y >= y:    # south-west
            self.sw = Leaf(self.x, self.y)

        elif self.x >= x and self.y < y:    # north-east
            self.ne = Leaf(self.x, self.y)

        elif self.x >= x and self.y >= y:   # south-east
            self.se = Leaf(self.x, self.y)
