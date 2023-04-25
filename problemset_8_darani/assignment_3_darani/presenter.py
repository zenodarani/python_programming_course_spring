from lliststack import Stack


# assignment 3.2
def print_stack(stk: Stack):
    ...  # TODO implement


if __name__ == '__main__':
    stk = Stack()
    for i in range(3):
        stk.push(i)
    print_stack(stk)
    print_stack(stk)
