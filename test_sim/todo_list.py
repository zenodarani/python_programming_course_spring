from priorityqueue import PriorityQueue, _PriorityQEntry


class ToDoList:

    HIGH = 0
    MEDIUM = 1
    LOW = 2

    def __init__(self):
        self._queue: PriorityQueue = PriorityQueue()

    def add(self, to_do: str, priority: int):
        self._queue.enqueue(to_do, priority)

    def remove_first(self):
        self._queue.dequeue()

    def __iter__(self):
        return _ToDoListIterator(self._queue)


class _ToDoListIterator:

    def __init__(self, queue: PriorityQueue):
        self._queue: PriorityQueue = queue
        self._tmp_queue: PriorityQueue = PriorityQueue()

    def __next__(self):
        try:
            item, priority = self._queue.dequeue()
        except AssertionError:
            raise StopIteration
        self._tmp_queue.enqueue(item, priority)
        return item

    def __iter__(self):
        return self


if __name__ == '__main__':
    myTodoList = ToDoList()
    myTodoList.add("wash laundry", 2)
    myTodoList.add("cook dinner", 1)
    myTodoList.add("make bed", 2)
    myTodoList.add("organise party", 0)
    myTodoList.add("book restaurant", 1)
    myTodoList.add("find a date", 0)
    for element in myTodoList:
        print(element)
