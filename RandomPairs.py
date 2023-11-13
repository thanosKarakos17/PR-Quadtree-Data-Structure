import random
from random import randint


class RandomPairs:
    def __init__(self):
        self.pairs = set()

    def random_pairs(self, m, n):
        while len(self.pairs) < m:      # creates a set with random pairs (x,y), sets contain only unique elements
            x = randint(0, n - 1)
            y = randint(0, n - 1)
            dict1 = (x, y)
            self.pairs.add(dict1)
        return self.pairs.copy()

    def non_existing_pairs(self, n):
        non_exist = set()
        while len(non_exist) < 100:
            x = randint(0, n - 1)
            y = randint(0, n - 1)
            dict2 = (x, y)
            dict1 = set()
            dict1.add(dict2)
            non_exist.update(dict1 - self.pairs)    #(x,y) is inserted if it doesn't exist in the initial set

        return non_exist

    def existing_pairs(self, n):
        exist = set()                   #randomly selects 100 elements from the whole set
        while len(exist) < 100:
            exist.add(random.choice(tuple(self.pairs)))
        return exist
