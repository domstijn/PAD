"""

creating a linked list

"""
from typing import Any


class Node:
    def __init__(self, data: Any, next_=None):
        self.data = data
        self.next = next_

    def __repr__(self):
        return f"{self.data}"


class LinkedList:
    def __init__(self, name):
        self.name = name
        self.head = None
        self.size = 0
        self.is_reversed = False
        self.type_class: Node = Node

    def __repr__(self):
        if self.empty:
            return "-- empty linked list --"
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
    def empty(self):
        if self.head is None:
            return True
        return False

    def prepend(self, data):
        """
        adds node to the head of the list, effectively nudging the list one place forward
        """
        if isinstance(data, list):
            for entry in data:
                self.prepend(entry)
            return

        new_node = self.type_class(data)

        if self.empty:
            self.head = new_node
        else:
            # else add the current head as the next node of the current
            new_node.next = self.head
            self.head = new_node

        self.size += 1
        return

    def append(self, data):
        if isinstance(data, list):
            for entry in data:
                self.append(entry)
            return

        if self.empty:
            self.prepend(data)

        else:
            # go over all the nodes, till the last node's next is None
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            new_node = self.type_class(data)
            current_node.next = new_node

            self.size += 1

        return

    def pop_head(self):
        if self.empty:
            return None

        head_node = self.head
        # remove the node as the head
        self.head = head_node.next

        self.size -= 1
        return head_node

    def pop_tail(self):
        if self.empty:
            return None

        tail_node = self.head
        while True:
            second_to_last_node = tail_node
            tail_node = tail_node.next

            if tail_node.next is None:
                second_to_last_node.next = None
                return tail_node

    def find(self, data):
        # NOTE when the data is an object instance, it needs to have an __eq__ method to be able to find a match
        if self.empty:
            return None

        current_node = self.head
        while current_node.data != data:
            current_node = current_node.next

            if current_node is None:
                return None

        return current_node

    def reverse(self):
        """
        reverses the linked list in place,
        maybe include a possibility to make a reversed copy
        """
        if self.empty:
            return

        prev_node = None
        current_node = self.head
        next_node = current_node.next

        while True:
            current_node.next = prev_node

            prev_node = current_node
            current_node = next_node
            next_node = next_node.next

            if next_node is None:
                current_node.next = prev_node
                self.head = current_node
                break

        self.is_reversed = not self.is_reversed

        return


if __name__ == '__main__':
    linked_a = LinkedList("linked A -- app")

    linked_a.append(['a', 'b', 'c', 'd', 'e', 'f'])

    print(linked_a)

    linked_b = LinkedList("linked B -- pre")

    linked_b.prepend(['a', 'b', 'c', 'd', 'e', 'f'])

    print(linked_b)

    linked_b.reverse()

    print(linked_b)
