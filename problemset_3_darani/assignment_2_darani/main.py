from linearmap import Map

if __name__ == '__main__':
    # Test Assignment 2.3 e 2.4
    m = Map()
    m.add('foo', 1)
    m.add('bar', 3)
    m.add('baz', 3)
    print('Assignment 2.3')
    print(m.keyArray())
    print('\nAssignment 2.4')
    for entry in m:
        print(f'{entry.key} - {entry.value}')
