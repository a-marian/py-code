import unittest
import Doubly_LinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()

    def test_empty_list(self):
        # Edge: Start with an empty list
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(self.dll.traverse(), [])

    def test_add_single_node(self):
        # Edge: Add a single node to an empty list
        n = self.dll.add_node(5)
        self.assertIs(self.dll.head, n)
        self.assertIs(self.dll.tail, n)
        self.assertIsNone(n.prev)
        self.assertIsNone(n.next)
        nodes = self.dll.traverse()
        self.assertEqual(len(nodes), 1)
        self.assertIs(nodes[0], n)

    def test_add_multiple_nodes(self):
        # Add several nodes and check structure
        n1 = self.dll.add_node(1)
        n2 = self.dll.add_node(2)
        n3 = self.dll.add_node(3)
        self.assertIs(self.dll.head, n1)
        self.assertIs(self.dll.tail, n3)

        self.assertIs(n1.next, n2)
        self.assertIs(n2.prev, n1)
        self.assertIs(n2.next, n3)
        self.assertIs(n3.prev, n2)

        nodes = self.dll.traverse()
        self.assertEqual([node.data for node in nodes], [1,2,3])

    def test_manual_link_nodes(self):
        # Edge: Manually link two nodes not at the end
        n1 = Node(10)
        n2 = Node(20)
        self.dll.link_nodes(n1, n2)
        self.assertIs(n1.next, n2)
        self.assertIs(n2.prev, n1)

    def test_traverse_empty_list(self):
        # Edge: Traverse without any nodes added
        self.assertEqual(self.dll.traverse(), [])

    def test_traverse_after_manual_link(self):
        # Edge: Create a chain manually and try traverse
        n1 = Node(9)
        n2 = Node(8)
        n3 = Node(7)
        self.dll.head = n1
        self.dll.tail = n3
        self.dll.link_nodes(n1, n2)
        self.dll.link_nodes(n2, n3)
        nodes = self.dll.traverse()
        self.assertEqual([node.data for node in nodes], [9,8,7])

    def test_link_node_to_none(self):
        # Edge: Link a node to None
        n = Node(100)
        self.dll.link_nodes(n, None)
        self.assertIs(n.next, None)
        # This will fail if node2 is None, so your method may need guarding

    def test_circular_reference(self):
        # Edge: Create circular references and ensure traverse does not infinitely loop.
        n1 = self.dll.add_node(1)
        n2 = self.dll.add_node(2)
        n1.prev = n2
        n2.next = n1
        # Now head: n1.next==n2, n2.next==n1 (circle). Traverse should not infinitely loop
        # But as defined, traverse traverses till current is None, so it won't get stuck unless we change the code.
        # We can check only traverses two nodes
        nodes = self.dll.traverse()
        self.assertEqual(len(nodes), 2)

if __name__ == "__main__":
    unittest.main()
