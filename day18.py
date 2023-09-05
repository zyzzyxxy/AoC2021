import math
from ast import literal_eval
from functools import reduce
last_explosion_from = ""

all_pairs = []

class Node():
    def __init__(self, value, level, parent, left_value = None, right_value = None):
        self.level = level
        self.value = value
        self.parent = parent
        self.left = left_value
        self.right = right_value
        self.exploded_right = False
        self.exploded_left = False
        self.explosion_in_branch = False
        self.string = ""

    def get_magnitude(self):
        left = 0
        right = 0
        if self.leftIsInt():
            left = self.left
        else:
            left = self.left.get_magnitude()
        if self.rightIsInt():
            right = self.right
        else:
            right = self.right.get_magnitude()

        sum = left*3+right*2
        return sum

    def reset(self):
        self.explosion_in_branch = False
        self.exploded_right = False
        self.exploded_left = False
        if self.have_left_tree():
            self.left.reset()
        if self.have_right_tree():
            self.right.reset()

    def increment_levels(self):
        self.level +=1
        if not self.leftIsInt():
            self.left.increment_levels()
        if not self.rightIsInt():
            self.right.increment_levels()

    def leftIsInt(self):
        return type(self.left) == int
    def rightIsInt(self):
        return type(self.right) == int

    def split_left(self):
        val = self.left
        left = val // 2
        right = math.ceil(val / 2)
        self.left = Node(-1, self.level+1, self, left, right)

    def split_right(self):
        val = self.right
        left = val // 2
        right = math.ceil(val / 2)
        self.right = Node(-1, self.level+1, self, left, right)

    def add_left(self, nbr):
        if not self.exploded_left:
            if type(self.left) is int:
                self.left += nbr
            else:
                self.left.add_closest_to_right(nbr)
        else:
            if self.parent:
                if self == self.parent.left:
                    self.parent.exploded_left = True
                self.parent.add_left(nbr)
            elif type(self.right) is not int and self.right.check_for_explosion_in_subtree():
                self.left.add_closest_to_right(nbr)

    def add_right(self, nbr):
        if not self.exploded_right:
            if type(self.right) is int:
                self.right += nbr
            else:
                self.right.add_closest_to_left(nbr)
        else:
            if self.parent:
                if self == self.parent.right:
                    self.parent.exploded_right = True
                self.parent.add_right(nbr)
            elif type(self.left) is not int and self.left.check_for_explosion_in_subtree():
                self.right.add_closest_to_left(nbr)

    def add_closest_to_left(self, nbr):
        if self.have_left_tree():
            self.left.add_closest_to_left(nbr)
        else:
            self.left +=nbr

    def add_closest_to_right(self, nbr):
        if self.have_right_tree():
            self.right.add_closest_to_right(nbr)
        else:
            self.right +=nbr

    def isLeaf(self):
        return type(self.left) is int and type(self.right) is int

    def explode(self):
        if self == self.parent.left:
            self.parent.exploded_left = True
            self.parent.left = 0
        elif self == self.parent.right:
            self.parent.exploded_right = True
            self.parent.right = 0
        self.parent.explosion_in_branch = True
        self.parent.add_right(self.right)
        self.parent.add_left(self.left)

    def get_string(self):
        string = "["
        if type(self.left) is int:
            string += (str(self.left))
        else:
            string +=(self.left.get_string())
        string +=","
        if type(self.right) is int:
            string +=(str(self.right))
        else:
            string +=(self.right.get_string())
        string +=("]")
        return string

    def have_left_tree(self):
        return type(self.left) is not int

    def have_right_tree(self):
        return type(self.right) is not int

    def check_for_explosion_in_subtree(self):
        if self.explosion_in_branch:
            return True
        else:
            if self.have_left_tree() and self.left.check_for_explosion_in_subtree():
                return True
            if self.have_right_tree() and self.right.check_for_explosion_in_subtree():
                return True
        return False

    def split(self):
        if self.have_left_tree():
            splitted = self.left.split()
            if splitted:
                return True
        else:
            if self.left > 9:
                self.split_left()
                return True
        if self.have_right_tree():
            splitted = self.right.split()
            if splitted:
                return True
        else:
            if self.right > 9:
                self.split_right()
                return True

        return False

def Add(node1, node2):
    node1.increment_levels()
    node2.increment_levels()
    new_root = Node(-1, 0, None, node1, node2)
    node1.parent = new_root
    node2.parent = new_root
    return new_root


def get_tree_from_array(pair, level, parent):
    node = Node(-1, level, parent)

    n1 = pair[0]
    n2 = pair[1]
    if type(n1) is int:
        node.left = n1
    else:
        node.left = get_tree_from_array(n1, level + 1, node)

    if type(n2) is int:
        node.right = n2
    else:
        node.right = get_tree_from_array(n2, level + 1, node)

    return node

def try_expload(root):
    # if root.level >= 4:
    #     if root.isLeaf():
    #         root.explode()
    #         return True
    #     else:
    #         if root.have_left_tree():
    #             try_expload(root.left)
    #         elif root.have_right_tree():
    #             try_expload(root.right)
    if root.level == 4:
        if root.isLeaf():
            root.explode()
            return True
    if type(root.left) != int:
        exp_left = try_expload(root.left)
        if exp_left:
            return True
    if type(root.right) != int:
        exp_right = try_expload(root.right)
        if exp_right:
            return True

    return False

def try_split(root):
    did_split = root.split()
    return did_split

def reduce_tree(root):
    exploaded = try_expload(root)
    if exploaded:
        print("exploaded")
        root.reset()
        return exploaded
    splitted = try_split(root)
    if splitted:
        root.reset()
        print("splitted")
    return splitted

def add_all_trees(tree_list):
    tree = tree_list[0]
    tree_list = tree_list[1:]
    running = True
    while running:
        running = reduce_tree(tree)
    for i in range(tree_list.__len__()):
        tree = Add(tree, tree_list[i])
        running = True
        while running:
            running = reduce_tree(tree)
    return tree

def run():
    #two_first = Add(literal_eval(pairs[0]), literal_eval(pairs[1]))
    def load_trees():
        trees = []
        pairs = open("day18").read().splitlines()
        for pair in pairs:
            pass
            tree = get_tree_from_array(literal_eval(pair), 0, None)
            trees.append(tree)
        return trees

    trees = load_trees()
    for tree in trees:
        break
        print(tree.get_string())
        reduce_tree(tree)
        print(tree.get_string())
        print("---------------")

    #test_tree = add_all_trees(trees)
    #print(test_tree.get_string())
    trees_len = trees.__len__()
    largest = 0
    for i in range(trees_len):
        for j in range(trees_len):
            if i!=j:
                trees = load_trees()
                node1 = trees[i]
                node2 = trees[j]
                test_tree = add_all_trees([node1, node2])
                running = True
                while running:
                    running = reduce_tree(test_tree)
                #print(test_tree.get_string())
                magnitude = test_tree.get_magnitude()
                #print(magnitude)
                if magnitude>largest:
                    largest=magnitude
    print(largest)

    #x = Explode(pairs, 0)
    #print(x)
    #5071 too high
run()