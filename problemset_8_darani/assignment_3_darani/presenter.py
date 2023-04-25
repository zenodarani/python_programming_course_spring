from lliststack import Stack


# assignment 3.2
def print_stack(stk: Stack):
    tmp_stk = Stack()
    stk_str = "TOP > ["
    while not stk.is_empty():
        item = stk.pop()
        stk_str += f" {item},"
        tmp_stk.push(item)
    stk_str = stk_str.removesuffix(",")
    stk_str += " ]"
    # Recompose the stuck
    while not tmp_stk.is_empty():
        stk.push(tmp_stk.pop())
    print(stk_str)


if __name__ == '__main__':
    stk = Stack()
    for i in range(3):
        stk.push(i)
    print_stack(stk)
    print_stack(stk)
