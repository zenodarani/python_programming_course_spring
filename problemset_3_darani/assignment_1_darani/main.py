import random
from linearset import Set


def randomSet(size, rndRange):
    rndSet = Set()
    for i in range(size):
        setSize = len(rndSet)
        while setSize == len(rndSet):
            rndSet.add(random.randint(*rndRange))
    return rndSet


if __name__ == '__main__':
    setA = randomSet(5, (1, 10))
    setB = randomSet(5, (1, 10))

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
