from circular_linked_list import CircularLinkedList


def print_list(my_list):
    print("List: ", end="")
    for item in my_list:
        print(item, end=", ")
    print("")


if __name__ == "__main__":

    # region Test Assignment 2.1
    clist = CircularLinkedList()
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
