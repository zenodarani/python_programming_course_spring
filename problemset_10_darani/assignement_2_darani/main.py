from circular_linked_list import CircularLinkedList


def print_list(my_list):
    print("List: ", end="")
    for item in my_list:
        print(item, end=", ")
    print("")


if __name__ == "__main__":

    # region Test Assignment 2.1 and 2.2
    print("---- Test Assignment 2.1 - 2.2 ----")
    clist = CircularLinkedList()
    print(f"Length of an empty list: {len(clist)}")
    # List [5, 4, 3, 2, 1]
    clist.push(1)
    clist.push(2)
    clist.push(3)
    clist.push(4)
    clist.push(5)

    print_list(clist)

    print(f"Length: {len(clist)}")
    print(f"Does list contain 3? {3 in clist}")
    print(f"Does list contain 11? {11 in clist}")
    print("Pop of the list:")
    print_list(clist)
    first_item = clist.pop()
    print_list(clist)
    print(f"First item removed from the list: {first_item}")
    # endregion

    # region Test Assignment 2.3
    print("\n---- Test Assignment 2.3 ----")
    clist2 = CircularLinkedList()
    clist2.push(3)
    clist2.push(7)
    clist2.push(11)
    clist2.push(1)

    print_list(clist2)
    print(f"Current item: {clist2.current()}")
    print(f"Next: {clist2.next()}")
    print(f"Peek Next: {clist2.peek_next()}")
    print(f"Next: {clist2.next()}")
    clist2.reset()
    print(f"Reset and show current: {clist2.current()}")
    # endregion
