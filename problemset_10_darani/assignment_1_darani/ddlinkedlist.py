class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    # -------------------------------------------------------------------------
    # assignment 1.1 basic functionality
    # -------------------------------------------------------------------------

    def __len__(self):
        cur_node = self._head
        length = 0
        while cur_node is not None:
            length += 1
            cur_node = cur_node.next

    def __iter__(self):
        return DoublyLinkedListIterator(self._head)

    def __reversed__(self):
        return ReverseLinkedListIterator(self._tail)

    def __getitem__(self, item):
        if type(item) != int or item < 0:
            raise IndexError("Index out of bound")
        cur_node = self._head
        for i in range(1, item + 1):
            if cur_node is None:
                raise IndexError("Index out of bound")
            cur_node = cur_node.next
        return cur_node.data

    def add_first(self, value):
        new_node = DoublyLinkedNode(value)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
            return
        new_node.next = self._head
        self._head.prev = new_node
        self._head = new_node

    def add_last(self, value):
        new_node = DoublyLinkedNode(value)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
            return
        self._tail.next = new_node
        new_node.prev = self._tail
        self._tail = new_node

    def contains(self, value):
        for item in self:
            if value == item:
                return True
        return False

    def clear(self):
        self._head = None
        self._tail = None

    def peek_first(self):
        if self._head is None:
            return None
        return self._head.data

    def peek_last(self):
        if self._tail is None:
            return None
        return self._tail.data

    def to_list(self):
        py_list = list()
        for item in self:
            py_list.append(item)
        return py_list

    # -------------------------------------------------------------------------
    # assignment 1.3 advanced functionality
    # -------------------------------------------------------------------------

    def current(self):
        # TODO implement
        ...

    def next(self):
        # TODO implement
        ...

    def prev(self):
        # TODO implement
        ...

    def peek_next(self):
        # TODO implement
        ...

    def peek_prev(self):
        # TODO implement
        ...

    def seek_head(self):
        # TODO implement
        ...

    def seek_tail(self):
        # TODO implement
        ...


# -------------------------------------------------------------------------
# assignment 1.2 support classes
# -------------------------------------------------------------------------
    
# service class node element
class DoublyLinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedListIterator:
    def __init__(self, head):
        self._cur_node = head

    def __next__(self):
        if self._cur_node is None:
            raise StopIteration()
        value = self._cur_node.data
        self._cur_node = self._cur_node.next
        return value

    def __iter__(self):
        return self


class ReverseLinkedListIterator:
    def __init__(self, tail):
        self._cur_node = tail

    def __next__(self):
        if self._cur_node is None:
            raise StopIteration()
        value = self._cur_node.data
        self._cur_node = self._cur_node.prev
        return value

    def __iter__(self):
        return self
