
class Person:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Height: {self.height}, Age: {self.age}"


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class OrderedByHeightList:

    def __init__(self, init_list):
        self._head = ListNode(init_list[0])
        cur_node = self._head
        for i in range(1, len(init_list)):
            cur_node.next = ListNode(init_list[i])
            cur_node = cur_node.next
        self._sort()

    def _sort(self):
        cur_node = self._head
        changes = False
        while changes:
            changes = False
            while cur_node is not None:
                if cur_node.value.height > cur_node.next.value.height:
                    next_ref = cur_node.next
                    cur_node.next = cur_node.next.next
                    next_ref.next = cur_node
                    # Flag that something changed
                    changes = True
                else:
                    # Go to the next node
                    cur_node = cur_node.next

    def __str__(self):
        str_desc = ""
        cur_node = self._head
        while cur_node is not None:
            str_desc += str(cur_node.value)


if __name__ == "__main__":
    peoples = [
        {
            "name": "Charles",
            "age": 28,
            "height": 182
        },
        {
            "name": "Anna",
            "age": 48,
            "height": 173
        },
        {
            "name": "Mike",
            "age": 12,
            "height": 165
        },
        {
            "name": "Zelda",
            "age": 32,
            "height": 168
        },
        {
            "name": "Matthew",
            "age": 61,
            "height": 175
        }]

    people_list = list()
    for person in peoples:
        people_list.append(Person(person["name"], person["height"], person["age"]))

    ordered_by_height = OrderedByHeightList(people_list)
    print(ordered_by_height)
