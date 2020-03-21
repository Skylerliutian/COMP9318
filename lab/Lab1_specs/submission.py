## import modules here
import math

################# Question 0 #################
def add(a, b): # do not change the heading of the function
    return a + b


################# Question 1 #################

def nsqrt(x): # do not change the heading of the function
    if x < 0:
        return
    if x < 2:
        return x
    head, tail = 0, x
    while head + 1 != tail:
        res = (head + tail) / 2
        if res ** 2 > x:
            tail = math.ceil(res)
        elif res ** 2 < x:
            head = math.floor(res)
        else:
            return int(res)
    return int(head)




################# Question 2 #################


# x_0: initial guess
# EPSILON: stop when abs(x - x_new) < EPSILON
# MAX_ITER: maximum number of iterations

## NOTE: you must use the default values of the above parameters, do not change them

def find_root(f, fprime, x_0=1.0, EPSILON = 1E-7, MAX_ITER = 1000): # do not change the heading of the function
    x_i = x_0
    for i in range(MAX_ITER):
        x_i_plus_1 = x_i - f(x_i) / fprime(x_i)
        if abs(x_i - x_i_plus_1) < EPSILON:
            break
        x_i = x_i_plus_1
    return x_i_plus_1


################# Question 3 #################

class Tree(object):
    def __init__(self, name='ROOT', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

def make_tree(tokens): # do not change the heading of the function
    t = Tree(tokens[0])
    root = t
    child = t
    root_list = []
    for i in range(1, len(tokens)):
        if tokens[i] == '[':
            root_list.append(root)
            root = child
        elif tokens[i] == ']':
            root = root_list.pop()
        else:
            child = Tree(tokens[i])
            root.add_child(child)
    return t


def max_depth(root): # do not change the heading of the function

    if root.children == 0:
        return 1
    depth = [1]
    for i in root.children:
        depth.append(max_depth(i) + 1)
    return max(depth)




