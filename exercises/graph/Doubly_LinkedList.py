## Do NOT modify this class.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return new_node

    def link_nodes(self, node1, node2):
        if node1 is not None:
            node1.next = node2
        if node2 is not None:
            node2.prev = node1
    def traverse(self):
        visited = []
        current = self.head
        while current:
            visited.append(current)
            current = current.next
        return visited

dll = DoublyLinkedList()
dll.add_node(1)
dll.add_node(2)
dll.add_node(3)

for node in dll.traverse():
    print(node.data)