from llistqueue import Queue


class QueuePresenter:

    @staticmethod
    def present(queue: Queue):
        print("<- [", end="")
        first = True
        for element in queue:
            if not first:
                print(",", end="")
            else:
                first = False
            print(f" {element}", end="")
        print(" ] <-")


if __name__ == "__main__":
    q = Queue()
    q.enqueue(9)
    q.enqueue(2)
    q.enqueue(1)
    QueuePresenter.present(q)
