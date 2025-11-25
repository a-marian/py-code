from __future__ import annotations
from typing import Generic, TypeVar, Optional, Any

T = TypeVar('T')


class Node(Generic[T]):
    """Internal node class for the doubly linked list."""
    __slots__ = ('data', 'prev', 'next')

    def __init__(self, data: T):
        self.data: T = data
        self.prev: Optional[Node[T]] = None
        self.next: Optional[Node[T]] = None

    def __repr__(self) -> str:
        return f"Node({self.data})"


class DoublyLinkedList(Generic[T]):
    """
    A fast doubly linked list with O(1) access to both head and tail.
    Supports any data type and efficient reverse printing.
    """

    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None   # Direct tail reference → O(1) access even with 10000+ nodes
        self._size: int = 0

    def append(self, data: T) -> None:
        """Add an element to the end of the list (O(1))"""
        new_node = Node(data)

        if self.tail is None:
            # First node
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def prepend(self, data: T) -> None:
        """Add an element to the beginning of the list (O(1))"""
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self._size += 1

    def get_tail(self) -> Optional[T]:
        """Return the data of the tail node in O(1) time"""
        return self.tail.data if self.tail else None

    def is_empty(self) -> bool:
        return self.head is None

    def size(self) -> int:
        return self._size

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        if self.is_empty():
            return "DoublyLinkedList([])"
        return f"DoublyLinkedList([{', '.join(repr(node.data) for node in self)}])"

    def __iter__(self):
        """Iterate from head to tail"""
        current = self.head
        while current:
            yield current
            current = current.next

    def reverse_iter(self):
        """Efficiently iterate from tail to head (O(1) start thanks to tail pointer)"""
        current = self.tail
        while current:
            yield current
            current = current.prev

    def print_reverse(self) -> None:
        """Print the list in reverse order efficiently"""
        if self.is_empty():
            print("[]")
            return

        items = [repr(node.data) for node in self.reverse_iter()]
        print(" ← ".join(items))

    def to_list(self) -> list[T]:
        """Convert to regular Python list (forward order)"""
        return [node.data for node in self]

    def to_list_reverse(self) -> list[T]:
        """Convert to regular Python list in reverse order efficiently"""
        return [node.data for node in self.reverse_iter()]


# ==================== Example Usage & Performance Test ====================

if __name__ == "__main__":
    # Test with mixed data types
    dll = DoublyLinkedList[Any]()
    dll.append("hello")
    dll.append(42)
    dll.append(3.14159)
    dll.append(None)
    dll.append([1, 2, 3])

    print("Forward:")
    print(dll)
    print("Reverse print:")
    dll.print_reverse()

    print(f"Tail (O(1) access): {dll.get_tail()}")

    # Performance test with 10,000+ elements
    print("\n" + "="*60)
    print("Performance test with 15,000 mixed elements...")

    import random
    dll_large = DoublyLinkedList[Any]()
    test_data = [
                    random.randint(-10000, 10000),
                    random.uniform(-1000, 1000),
                    f"string_{i}",
                    None,
                    (i, i*2),
                ] * 3000  # Will create 15,000 items

    for item in test_data:
        dll_large.append(item)

    print(f"List size: {len(dll_large)}")
    print(f"Tail accessed instantly: {dll_large.get_tail()}")
    print("First 10 items in reverse:")
    count = 0
    for node in dll_large.reverse_iter():
        print(node.data, end=" ← ")
        count += 1
        if count >= 10:
            print("...")
            break