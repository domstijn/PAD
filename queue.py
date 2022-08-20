from linked_list_double import Node, LinkedListDouble


class Entity(Node):
    def __init__(self, data):
        super().__init__(data)

    def __repr__(self):
        return f"Entity: {self.data}"

    def __str__(self):
        return f"{self.data}"


class Queue(LinkedListDouble):
    def __init__(self, name):
        super().__init__(name)
        self.type_class = Entity

    def __repr__(self):
        if self.is_empty:
            return "-- empty queue --"
        current_node = self.head

        representation = self.name + ": FRONT"

        while current_node is not None:

            representation += f" <-- {current_node}"

            current_node = current_node.next

        representation += " <-- BACK"

        if self.is_reversed:
            representation += " -- reversed! "

        return representation

    def enqueue(self, data):
        self.append(data)
        return

    def dequeue(self):
        if self.is_empty:
            print("NO NODES IN QUEUE")
            return
        return self.pop_head().data

    def next_in_line(self):
        return self.head


if __name__ == '__main__':
    queue = Queue("queue")

    queue.enqueue(['a', 'b', 'c', 'd', 'e', 'f'])

    print(queue)

    queue.dequeue()

    print(queue)

    queue.reverse()

    print(queue)

    queue.dequeue()

    print(queue)

    queue.reverse()

    print(queue)

    print(queue.next_in_line())


