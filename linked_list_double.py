"""

perfect double linked list

"""
from typing import Any


class Node:
    def __init__(self, data):
        self.data: Any = data
        self.next: Node = None
        self.prev: Node = None

    def __repr__(self):
        return f"N: {self.data}, prev -> {self.prev}, next -> {self.next}"

    def __str__(self):
        return f"{self.data}"


class LinkedListDouble:
    def __init__(self, name):
        self.name: str = name
        self.head: Node = None
        self.tail: Node = None
        self.size: int = 0
        self.is_reversed: bool = False
        self.type_class: Node = Node

    def __repr__(self):
        if self.is_empty:
            return "-- empty doubly-linked list --"
        current_node = self.head

        representation = self.name + ": HEAD"

        while current_node is not None:

            representation += f" --> {current_node}"

            current_node = current_node.next

        representation += " --> END"

        if self.is_reversed:
            representation += " -- reversed! "

        return representation

    @property
    def is_empty(self):
        return self.size == 0

    def prepend(self, data):
        if isinstance(data, list):
            for entry in data:
                self.prepend(entry)
            return

        new_node = self.type_class(data)

        if self.is_empty:
            self.head = new_node
            self.tail = new_node

        else:
            # beginning
            current_head = self.head
            self.head = new_node
            self.head.next = current_head  # new_node.next = current_head
            self.head.next.prev = self.head  # current_head.prev = new_node

        self.size += 1
        return

    def append(self, data):
        if isinstance(data, list):
            for entry in data:
                self.append(entry)
            return

        new_node = self.type_class(data)

        if self.is_empty:
            self.head = new_node
            self.tail = new_node

        else:
            current_tail = self.tail
            self.tail = new_node
            self.tail.prev = current_tail
            self.tail.prev.next = self.tail

        self.size += 1
        return

    def pop_head(self):
        if self.is_empty:
            return None

        current_head = self.head
        next_node = self.head.next

        if next_node is not None:
            next_node.prev = None
        else:
            self.tail = None

        self.head = next_node

        self.size -= 1

        return current_head

    def pop_tail(self):
        if self.is_empty:
            return None

        current_tail = self.tail
        prev_node = self.tail.prev

        if prev_node is not None:
            prev_node.next = None
        else:
            self.head = None

        self.tail = prev_node

        self.size -= 1

        return current_tail

    def find(self, data):
        """
        searches for first instance of node with the same data
        """
        if self.is_empty:
            return None

        current_node = self.head

        # search from beginning to end
        while current_node is not None:
            if current_node.data == data:
                return current_node
            current_node = current_node.next

        return None

    def find_all(self, data):
        """
        searches for all instances which have the same data
        """
        if self.is_empty:
            return None

        current_node = self.head
        found_nodes = list()

        while current_node is not None:
            if current_node.data == data:
                found_nodes.append(current_node)
            current_node = current_node.next

        if len(current_node) > 0:
            return found_nodes
        return None

    def remove(self, data):
        """
        only removes one node instance which matches with the data
        """
        node_to_remove = self.find(data)

        if node_to_remove is None:
            print("no node found with given data")
            return None

        prev_node = node_to_remove.prev
        next_node = node_to_remove.next

        if prev_node is not None:
            prev_node.next = next_node
        if next_node is not None:
            next_node.prev = prev_node

        return node_to_remove

    def reverse(self):
        if self.is_empty:
            return

        if self.head == self.tail:
            return

        current_node = self.head
        self.tail = current_node

        while current_node is not None:
            prev_node = current_node.prev
            next_node = current_node.next

            current_node.next = prev_node
            current_node.prev = next_node

            if next_node is None:
                self.head = current_node

            current_node = next_node

        self.is_reversed = not self.is_reversed


if __name__ == '__main__':
    double_ll_a = LinkedListDouble("double - b")
    double_ll_b = LinkedListDouble("double - a")

    double_ll_a.append(['a', 'b', 'c', 'd', 'e', 'f'])

    double_ll_b.prepend(['a', 'b', 'c', 'd', 'e', 'f'])

    print(double_ll_a)
    print(double_ll_b)

    double_ll_b.reverse()

    print(double_ll_b)


