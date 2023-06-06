import csv
from singly_linked_list import SinglyLinkedList, ListNode


class Student:
    def __init__(self, first_name, last_name, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = float(gpa)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.gpa}"


def parse_students(file_name):
    with open(file_name) as f:
        students_reader = csv.reader(f)
        return [Student(*s) for s in students_reader]


def _splitting(head: ListNode):
    mid_point: ListNode = head
    cur_node: ListNode = head.next
    while cur_node is not None:
        cur_node = cur_node.next
        if cur_node is not None:
            cur_node = cur_node.next
            mid_point = mid_point.next
    right_list = mid_point.next
    mid_point.next = None
    return right_list


# Given the head of a linked list, it performs a recursive merge sorting.
# It returns the reference of the head of the linked list after the ordering. The ordering is performed directly on the
# linked list!
# I chose the merge sort because is an excellent algorithm to sort a linked list.
def _recursive_merge_sort(list_head: ListNode, ascending=True):
    left_list = list_head
    order = 1 if ascending else -1
    # splitting
    right_list = _splitting(left_list)
    if right_list is not None:
        sorted_left_list = _recursive_merge_sort(left_list, ascending)
        sorted_right_list = _recursive_merge_sort(right_list, ascending)
        # merging
        if order * sorted_left_list.data.gpa < order * sorted_right_list.data.gpa:
            merged_list = sorted_left_list
            sorted_left_list = sorted_left_list.next
            merged_list.next = None
        else:
            merged_list = sorted_right_list
            sorted_right_list = sorted_right_list.next
            merged_list.next = None
        cur_node = merged_list
        while sorted_left_list is not None and sorted_right_list is not None:
            if order * sorted_left_list.data.gpa < order * sorted_right_list.data.gpa:
                cur_node.next = sorted_left_list
                sorted_left_list = sorted_left_list.next
                cur_node = cur_node.next
                cur_node.next = None
            else:
                cur_node.next = sorted_right_list
                sorted_right_list = sorted_right_list.next
                cur_node = cur_node.next
                cur_node.next = None
        if sorted_left_list is not None:
            cur_node.next = sorted_left_list
        elif sorted_right_list is not None:
            cur_node.next = sorted_right_list
        return merged_list
    else:
        # when it reaches the end of the tree
        return left_list


# returns a singly linked list with sorted elements
def merge_sort(students, ascending=True):
    # creating a linked list
    students_llist = SinglyLinkedList()
    for st in students:
        students_llist.add_node(st)

    # recursive merge sort with linked list
    new_head = _recursive_merge_sort(students_llist._head, False)
    students_llist._head = new_head
    return students_llist


if __name__ == '__main__':
    students = parse_students("gpa.csv")
    sorted_students: SinglyLinkedList = merge_sort(students, ascending=False)
    print("Top students:")
    print("____________________________________________")
    c = 1
    for std in sorted_students:
        print(f"Ranking #{c}", end="\t")
        print(std)
        c += 1
        if c == 11:
            break
