# This is a sample Python script.
from KD_tree import KD_tree
from Leaf import Leaf
from Node import Node
from PR_quadtree import PR_quadtree
from RandomPairs import RandomPairs


def plant_kd_tree(set1, m):  # iterate over the set that contains M unique pairs and insert each 'node' on KD_TREE
    tree = KD_tree()
    for pair in set1:
        (x, y) = pair
        node = Node(x, y)
        tree.insert(node)
    return tree


def plant_pr_quadtree(set1, m):  # iterate over the set that contains M unique pairs and insert each 'leaf' on PR_QUADTREE
    tree = PR_quadtree()
    for pair in set1:
        (x, y) = pair
        node = Leaf(x, y)
        tree.insert(node)
    return tree


def search_kd_tree(tree, pairs):    # iterate over the set (either contains existing nodes or non existing nodes)
    count = 0                       # search each node inside the KD_TREE and calculate the sum of the levels the tree reached
    for pair in pairs:
        (x, y) = pair
        node = Node(x, y)
        count += tree.search(node)
    return count / 100              # return the average level (we perform 100 searches)


def search_pr_quadtree(tree, pairs):    # iterate over the set (either contains existing leaves or non existing leaves)
    count = 0                           # search each node inside the PR_QUADTREE and calculate the sum of the levels the tree reached
    for pair in pairs:
        (x, y) = pair
        node = Leaf(x, y)
        count += tree.search(node)
    return count / 100                  # return the average level (we perform 100 searches)


def main():
    M = [200, 500, 1000, 10000, 30000, 50000, 70000, 100000]
    N = 2 ** 16

    print(' \t\t\t\tKD Tree \tPR Quadtree')
    print(' \t\t\texist nonexist\texist nonexist')
    # loop over different values of M
    for m in M:
        rand = RandomPairs()
        pairs = rand.random_pairs(m, N)             # create a set of unique pairs size m
        kd_tree = plant_kd_tree(pairs, m)           # create kd_tree
        pr_quadtree = plant_pr_quadtree(pairs, m)   #create pr_quadtree
        non_exist = rand.non_existing_pairs(N)      # create a set of non existing elements from the 'pairs' set size 100
        exist = rand.existing_pairs(N)              # create a set of exisitng elements from the 'pairs' set size 100

        count1_exist = search_kd_tree(kd_tree, exist)
        count1_non_exist = search_kd_tree(kd_tree, non_exist)

        count2_exist = search_pr_quadtree(pr_quadtree, exist)
        count2_non_exist = search_pr_quadtree(pr_quadtree, non_exist)

        print(f"M\t{len(pairs)} \t{count1_exist} \t{count1_non_exist} \t{count2_exist} \t{count2_non_exist}")


if __name__ == '__main__':
    main()
