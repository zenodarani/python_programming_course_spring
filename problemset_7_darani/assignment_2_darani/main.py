from singly_linked_list import SinglyLinkedList


def test_assignment_2_0():
    # test __str__
    sll = SinglyLinkedList()
    assert str(sll) == "[]", "__str__ not implemented correctly on empty list"

    # test __str__ and add_node
    sll.add_node(0)
    sll.add_node(1)
    sll.add_node(2)
    assert str(
        sll) == "[2, 1, 0, ]", "__str__ or add_node not implemented correctly"

    # test __contains__
    assert 2 in sll, "__contains__ not implemented correctly"
    assert -1 not in sll, "__contains__ not implemented correctly"

    # test remove_node
    sll.remove_node(2)
    assert 2 not in sll, "remove_node not implemented correctly"
    try:
        sll.remove_node(2)
        assert False, "remove_node does not throw a ValueErrror"
    except ValueError:
        pass

    print("Assignment 2.0 -> OK")


def test_assignment_2_1():
    sll = SinglyLinkedList()
    sll.add_node(0)
    sll.add_node(1)
    sll.add_node(2)

    # test __len___
    assert len(SinglyLinkedList()) == 0, "__len__ not implemented correctly"
    assert len(sll) == 3, "__len__ not implemented correctly"

    # test the iterator
    assert list(sll) == [2, 1, 0], "Iterator not implemented correctly"

    # test __getitem__
    try:
        sll["error"]
        assert False, "should raise ValueError on non-integer key"
    except ValueError:
        pass
    try:
        sll[10]
        assert False, "should raise IndexError on non-integer key"
    except IndexError:
        pass
    assert sll[0] == 2, "__getitem__ not implemented correctly"

    # test clear
    sll.clear()
    assert len(sll) == 0, "clear not implemented correctly"

    # test swap
    sll.add_node(0)
    sll.add_node(1)
    sll.add_node(2)
    sll.swap_nodes(0, 2)
    assert str(sll) == "[0, 1, 2, ]", "swap not implemented correctly"

    print("Assignment 2.1 -> OK")


def assignment_2_2():
    print("-- ASSIGNMENT 2.2 --")
    print("Creating list with elements ", end="")
    sll = SinglyLinkedList()
    sll.add_node(0)
    sll.add_node(1)
    sll.add_node(2)
    print(sll)

    print("Swapping first and last values, before: ", end="")
    print(sll)
    first = sll[0]
    last = sll[-1]
    sll.swap_nodes(first, last)
    print("After swap: ", end="")
    print(sll)

    print("Removing all: ", end="")
    sll.clear()
    print(sll)
    print()


if __name__ == '__main__':
    test_assignment_2_0()
    test_assignment_2_1()
