from typing import Optional


class CircularLinkedList:
    def __init__(self):
        self._head: Optional[LinkedNode] = None
        self._tail: Optional[LinkedNode] = None
        
    # -------------------------------------------------------------------------
    # assignment 1.1 basic functionality
    # -------------------------------------------------------------------------

    def __iter__(self):
        return CircularListIterator(self._head)

    def __len__(self):
        count = 0
        for node in self:
            count += 1
        return count

    def __contains__(self, item):
        for node in self:
            if node.data == item:
                return True
        return False

    def push(self, item):
        new_node = LinkedNode(item, self._head)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        self._head = new_node
        self._tail.next = new_node

    def pop(self, item):
        self._tail.next = self._head.next
        self._head = self._head.next

    def is_empty(self):
        # TODO implement
        ...

    def current(self):
        # TODO implement
        ...

    def next(self):
        # TODO implement
        ...

    def peek_next(self):
        # TODO implement
        ...

    def reset(self):
        # TODO implement
        ...


class LinkedNode:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

    def __str__(self):
        return f"{self.data}"
    
    def __repr__(self) -> str:
        return self.__str__()


class CircularListIterator:
    def __init__(self, head):
        self._head = head
        self._curr = head
        self._first = True

    def __next__(self):
        if self._head == self._curr and not self._first:
            raise StopIteration()
        value = self._curr.data
        self._curr = self._curr.next
        return value

    def __iter__(self):
        return self
