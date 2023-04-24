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
        if self._head is None:
            return 0
        length = 1
        cur_node = self._head
        while cur_node.next:
            length += 1
            cur_node = cur_node.next
        return length

    def __iter__(self):
        return LinkedListIterator(self._head)

    def __getitem__(self, item):
        if type(item) != int:
            raise ValueError("index must be an integer")
        if item < 0:
            raise IndexError("index must be positive")
        cur_node = self._head
        for i in range(item):
            if not cur_node.next:
                raise IndexError("index out of bound")
            cur_node = cur_node.next
        return cur_node.data

    def clear(self):
        self._head = None

    def swap_nodes(self, idx_a: int, idx_b: int):
        if idx_a < 0 or idx_b < 0:
            raise IndexError("index must be positive")
        if idx_a == idx_b:
            return
        max_idx = max(idx_a, idx_b)
        min_idx = min(idx_a, idx_b)
        min_node = None
        max_node = None
        min_pre_node = None
        max_pre_node = None
        cur_node = self._head
        for i in range(max_idx):
            if i == 0 and min_idx == 0:
                min_node = cur_node
            if i == min_idx - 1:
                min_pre_node = cur_node
                min_node = cur_node.next
            if i == max_idx - 1:
                max_pre_node = cur_node
                max_node = cur_node.next
            cur_node = cur_node.next
            # end of the list
            if cur_node is None:
                raise IndexError("index out of bound")

        if min_pre_node is None:
            self._head = max_node
        else:
            min_pre_node.next = max_node
        max_pre_node.next = min_node
        min_node_next = min_node.next
        min_node.next = max_node.next
        max_node.next = min_node_next

            

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

