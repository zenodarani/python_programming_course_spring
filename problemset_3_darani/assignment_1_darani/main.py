import random
from linearset import Set


def getRandomSet(size, rndRange):
    rndSet = Set()
    for i in range(size):
        setSize = len(rndSet)
        while setSize == len(rndSet):
            rndSet.add(random.randint(*rndRange))
    return rndSet


if __name__ == '__main__':
    # region Assignment 1.1
    setA = getRandomSet(5, (1, 10))
    setB = getRandomSet(5, (1, 10))

    print('Assignment 1.1')
    print('Set A')
    print(setA)
    print('Set B')
    print(setB)
    print('Intersection A, B')
    print(setA.intersect(setB))
    print('Difference A - B')
    print(setA.difference(setB))
    print('Difference B - A')
    print(setB.difference(setA))
    # endregion

    # region Assignment 1.2
    initValues = [12, 5, 23, 23, 6]
    setC = Set(*initValues)

    print('\nAssignment 1.2')
    print(f'initValues = {initValues}')
    print(f'setC = Set(*initValues)')
    print(f'Set C -> {setC}')
    # endregion
