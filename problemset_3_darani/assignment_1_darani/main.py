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

    # region Assignment 1.3
    setA = Set(2, 0, 1)
    setB = Set(2, 0, 1)
    setC = Set(2, 0)
    print('\nAssignment 1.3')
    print(f'Set A -> {setA}')
    print(f'Set B -> {setB}')
    print(f'Set C -> {setC}')
    print(f'Is set A subset of B? {setA.isSubsetOf(setB)}')
    print(f'Is set A proper subset of B? {setA.isProperSubsetOf(setB)}')
    print(f'Is set C proper subset of A? {setC.isProperSubsetOf(setA)}')
    # endregion