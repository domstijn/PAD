from linked_list_single import Node, LinkedList


class Task(Node):
    def __init__(self, data):
        super().__init__(data)


class Stack(LinkedList):
    def __init__(self, name: str, size_limit: int):
        super().__init__(name)
        self.size_limit = size_limit

    def __repr__(self):
        if self.empty:
            return "-- empty stack --"
        current_node = self.head

        representation = self.name + ": TOP"

        while current_node is not None:

            representation += f" --> {current_node}"

            current_node = current_node.next

        representation += " --> BOTTOM"

        if self.is_reversed:
            representation += " -- reversed! "

        return representation

    def __str__(self):
        if self.empty:
            return "[-- empty stack --]"
        current_node = self.head

        representation = "[" + f"{current_node}"

        while current_node.next is not None:
            current_node = current_node.next

            representation += f", {current_node}"

        representation += "]"

        if self.is_reversed:
            representation += " -- reversed! "

        return representation

    @property
    def full(self):
        return self.size == self.size_limit

    def push(self, data):
        if self.full:
            print("STACK OVERFLOW")
            return
        self.prepend(data)

    def pop(self):
        if self.empty:
            print("STACK UNDERFLOW")
            return
        return self.pop_head().data

    def peek(self):
        return self.head.data


if __name__ == '__main__':
    stack = Stack('stack', 10)
    stack.type_class = Task

    stack.push(['1', '2', '3', '4', '5', '6', '7'])

    print(stack)

    stack.pop()

    print(stack)

    stack.reverse()

    print(stack)

