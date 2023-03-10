# Implementation of the Set ADT container using a Python list.
class Set:
    def __init__(self, *initElements):
        self._theElements = list()
        for element in initElements:
            self.add(element)

    # Returns the number of items in the set.
    def __len__(self):
        return len(self._theElements)

    # Determines if an element is in the set.
    def __contains__(self, element):
        return element in self._theElements

    # Adds a new unique element to the set.
    def add(self, element):
        if element not in self:
            self._theElements.append(element)

    # Removes an element from the set.
    def remove(self, element):
        assert element in self, "The element must be in the set."
        self._theElements.remove(element)

    # Determines if two sets are equal.
    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)

    # Determines if this set is a subset of setB.
    def isSubsetOf(self, setB):
        for element in self._theElements:
            if element not in setB:
                return False
        return True

    # Determines if this set is a proper subset of another given set (setB).
    def isProperSubsetOf(self, setB):
        return self.isSubsetOf(setB) and len(self) != len(setB)

    # Creates a new set from the union of this set and setB.
    def union(self, setB):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB._theElements:
            if element not in self:
                newSet._theElements.append(element)
        return newSet

    # Creates a new set from the intersection of this set and setB.
    def intersect(self, setB):
        intersectionSet = Set()
        for selfSetElement in self._theElements:
            if selfSetElement in setB:
                intersectionSet.add(selfSetElement)
        return intersectionSet

    # Creates a new set from the difference of this set and setB
    def difference(self, setB):
        intersectionSet = self.intersect(setB)
        differenceSet = Set()
        for element in self._theElements:
            if element not in intersectionSet:
                differenceSet.add(element)
        return differenceSet

    # Returns an iterator for traversing the list of items.
    def __iter__(self):
        return _SetIterator(self._theElements)

    # Returns a sting representation of the Set
    def __str__(self):
        elementsLength = len(self._theElements)
        setStr = '{'
        for i in range(elementsLength-1):
            setStr += f'{self._theElements[i]}, '
        if elementsLength > 0:
            setStr += f'{self._theElements[-1]}}}'
        else:
            setStr += ' }'
        return setStr

    # Does the union of this set and another given setB
    def __add__(self, setB):
        return self.union(setB)

    # Does the intersection of this set and another given setB
    def __mul__(self, setB):
        return self.intersect(setB)

    # Does the difference of this set with a given setB
    def __sub__(self, setB):
        return self.difference(setB)

    # States if this set is a subset of a given setB
    def __lt__(self, setB):
        return self.isSubsetOf(setB)


# Iterator class for Set
class _SetIterator:
    def __init__(self, theElements):
        self._theElements = theElements
        self._curIndex = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curIndex < len(self._theElements):
            entry = self._theElements[self._curIndex]
            self._curIndex += 1
            return entry
        else:
            raise StopIteration
