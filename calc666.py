#!/usr/bin/env python

import sys

class Node:
    def __init__(self, value, parent, operator, partner=None, constructable=False):
        self.value = value
        self.parent = parent
        self.constructable = constructable
        if operator in ["unary", "binary", "root"]:
            self.operator = operator
        else:
            raise Exception("operator has to be either unary or binary")
        self.partner = None
        self.unary_children = []
        self.binary_children = []

    def set_constructable(self):
        self.constructable = True
        if self.operator == "unary":
            self.parent.set_constructable()
        elif self.operator == "binary" and self.partner.constructable:
            self.parent.set_constructable()

    def __str__(self):
        if self.operator == "root":
            return str(self.value)
        # if self.operator == "unary":
        if self.partner:
            return("{}->{}".format((self.value, self.partner.value), self.parent))
        return("{}->{}".format(self.value, self.parent))
        # return "Not implemented"


class Calc666:
    def __init__(self, disallowed_keys, unary_inverse=None, binary_inverse=None):
        if unary_inverse:
            self.unary_inverse = unary_inverse
        if binary_inverse:
            self.binary_inverse = binary_inverse
        self.disallowed_keys = disallowed_keys
        self.root = Node(666, None, "root")

    def is_allowed(self, value):
        for key in self.disallowed_keys:
            if key in format(value, "g"):
                return False
        return True

    def generate_values_unary(self, node):
        self.add_node(node, self.unary_inverse(node.value), "unary")
        self.add_node(node, self.unary_inverse(-node.value), "unary")

    def add_node(self, parent, new_value, operation):
        new_node = Node(new_value, parent, operation)
        if operation == "unary":
            if self.is_allowed(new_value):
                parent.set_constructable()
                if self.root.constructable:
                    print(new_node)
                    sys.exit(0)
            parent.unary_children.append(new_node)
        return new_node

    def node_pairs(self, results, val, parent):
        pairs = []
        if len(results) >= 1:
            node1 = Node(results[0], parent, "binary")
            node2 = Node(val, parent, "binary")
            node1.partner = node2
            node2.partner = node1
            pairs.append((node1, node2))
        if len(results) >= 2:
            node1 = Node(val, parent, "binary")
            node2 = Node(results[1], parent, "binary")
            node1.partner = node2
            node2.partner = node1
            pairs.append((node1, node2))
        return pairs

    def add_nodes_binary(self, node, val):
        node.binary_children.extend(self.node_pairs(self.binary_inverse(node.value, val), val, node))
        node.binary_children.extend(self.node_pairs(self.binary_inverse(-node.value, val), val, node))
        node.binary_children.extend(self.node_pairs(self.binary_inverse(node.value, -val), -val, node))
        node.binary_children.extend(self.node_pairs(self.binary_inverse(-node.value, -val), -val, node))
        for n1, n2 in node.binary_children:
            if self.is_allowed(n1.value):
                n1.set_constructable()
            if self.is_allowed(n2.value):
                n2.set_constructable()
            if self.root.constructable:
                print(n1)
                sys.exit(1)


# if __name__ == "__main__":
