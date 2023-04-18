from __future__ import annotations
from typing import Any, Tuple


class SinglyLinkedList:

    def __init__(self):
        self._head = None

    def __str__(self):
        curr_node = self._head
        res_string = "["
        while curr_node is not None:
            res_string += str(curr_node.data) + ", "
            curr_node = curr_node.next
        res_string += "]"
        return res_string

    def __contains__(self, item: Any) -> bool:
        curr_node = self._head
        while curr_node is not None and curr_node.data != item:
            curr_node = curr_node.next
        return curr_node is not None

    def add_node(self, value: Any) -> Any:
        new_node = ListNode(value)
        new_node.next = self._head
        self._head = new_node
        return new_node.data

    def remove_node(self, target) -> Any:
        pred_node = None
        cur_node = self._head

        while cur_node is not None and cur_node.data != target:
            pred_node = cur_node
            cur_node = cur_node.next

        # end of cycle and not found
        if cur_node is None:
            raise ValueError(f"{target} is not contained in the list!")

        if cur_node is self._head:
            self._head = cur_node.next
        else:
            pred_node.next = cur_node.next

        return cur_node.data

    def __len__(self):
        ...  # TODO implement

    def __iter__(self):
        return LinkedListIterator(self._head)

    def __getitem__(self, item):
        ...  # TODO implement

    def clear(self):
        ...  # TODO implement

    def swap_nodes(self, idx_a: int, idx_b: int):
        ...  # TODO implement


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListIterator:
    def __init__(self, head):
        self.head = head

    def __next__(self):
        cur_node = self.head
        if cur_node:
            self.head = self.head.next
            return cur_node.data
        raise StopIteration()

    def __iter__(self):
        return self

