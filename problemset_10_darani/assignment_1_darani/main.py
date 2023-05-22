from ddlinkedlist import DoublyLinkedList

if __name__ == "__main__":

    # region Test for assignment 1.1 and 1.2
    print("---- Test Assignments 1.1 and 1.2 ----")
    ddlist = DoublyLinkedList()
    # list from head to tail: 1 3 2 7 8 2 5 4
    ddlist.add_first(7)
    ddlist.add_first(2)
    ddlist.add_first(3)
    ddlist.add_last(8)
    ddlist.add_last(2)
    ddlist.add_last(5)
    ddlist.add_first(1)
    ddlist.add_last(4)

    print("From head to tail: ", end="")
    for item in ddlist:
        print(item, end=", ")
    print("")

    print("From tail to head: ", end="")
    for item in reversed(ddlist):
        print(item, end=", ")
    print("")

    print(f"Does the list contain 5 ? {ddlist.contains(5)}")
    print(f"Does the list contain 11 ? {ddlist.contains(11)}")

    print(f"First element: {ddlist.peek_first()}")
    print(f"Last element: {ddlist.peek_last()}")

    print(f"Getting the item at index 5: {ddlist[5]}")
    print(f"Getting the item at index 0: {ddlist[0]}")

    print(f"Getting the item at index 12: ", end="")
    try:
        ddlist[12]
    except IndexError as ie:
        print(ie.args[0])
    print(f"Getting the item at index -1: ", end="")
    try:
        ddlist[-1]
    except IndexError as ie:
        print(ie.args[0])

    print(f"To Python list: {ddlist.to_list()}")

    ddlist.clear()
    print(f"Clear: {ddlist.to_list()}")
    print(f"First element after clear: {ddlist.peek_first()}")
    print(f"Last element after clear: {ddlist.peek_last()}")
    print("Item at index 5 after clear: ", end="")
    try:
        ddlist[5]
    except IndexError as ie:
        print(ie.args[0])
    # endregion

    # region Test for assignment 1.3
    print("\n---- Test Assignment 1.3 ----")
    ddlist2 = DoublyLinkedList()
    # List -> [1, 5, 8, 3, 6, 4]
    ddlist2.add_last(1)
    ddlist2.add_last(5)
    ddlist2.add_last(8)
    ddlist2.add_last(3)
    ddlist2.add_last(6)
    ddlist2.add_last(4)
    print("List from head to tail: ", end="")
    for item in ddlist2:
        print(item, end=", ")
    print()
    print(f"Current: {ddlist2.current()}")
    print(f"Next: {ddlist2.next()}")
    print(f"Next: {ddlist2.next()}")
    print(f"Previous: {ddlist2.prev()}")
    print(f"Peek next: {ddlist2.peek_next()}")
    print(f"Current: {ddlist2.current()}")
    print(f"Peek prev: {ddlist2.peek_prev()}")
    print(f"Current: {ddlist2.current()}")
    print(f"Seek head: {ddlist2.seek_head()}")
    print(f"Current: {ddlist2.current()}")
    print(f"Seek tail: {ddlist2.seek_tail()}")
    print(f"Current: {ddlist2.current()}")
    # endregion
