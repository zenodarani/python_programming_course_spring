# Implementation of the Map ADT using closed hashing and a probe with # double hashing.
from array_adt import Array


# Storage class for holding the key/value pairs.
class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap:
    # Defines constants to represent the status of each table entry.
    UNUSED = None
    EMPTY = _MapEntry(None, None)
    INIT_M = 7

    # Creates an empty map instance.
    def __init__(self):
        self._table = Array(self.INIT_M)
        for i in range(len(self._table)):
            self._table[i] = HashMap.UNUSED
        self._count = 0
        self._maxCount = len(self._table) - len(self._table) // 3

    # Returns the number of entries in the map.
    def __len__(self):
        return self._count

    # Determines if the map contains the key
    def __contains__(self, key):
        slot = self._find_slot(key, False)
        return slot is not None

    # adds a new entry to the map if key does not exist. Otherwise, the
    # new value replaces the current value associated with the key.
    def add(self, key, value):
        if key in self:
            slot = self._find_slot(key, False)
            self._table[slot].value = value
            return False
        else:
            slot = self._find_slot(key, True)
            self._table[slot] = _MapEntry(key, value)
            self._count += 1
            if self._count == self._maxCount:
                self._rehash()
            return True

    # Returns the value associated with the key.
    def value_of(self, key):
        slot = self._find_slot(key, False)
        if slot is None:
            raise IndexError("Invalid map key.")
        return self._table[slot].value

    # Removes the entry associated with the key.
    def remove(self, key):
        slot = self._find_slot(key, False)
        if slot is None:
            raise IndexError("Key is not contained")
        value = self._table[slot].value
        self._table[slot] = self.UNUSED
        return value
        
    # Finds the slot containing the key or where the key can be added.
    # forInsert indicates if the search is for an insertion, which locates
    # the slot into which the new key can be added.
    def _find_slot(self, key, forInsert):
        # Compute the home slot and the step size.
        slot = self._hash1(key)
        step = self._hash2(key)
        # Probe for the key.
        M = len(self._table)
        if forInsert:
            while self._table[slot] is not self.UNUSED and self._table[slot] is not self.EMPTY:
                slot = (slot + step) % M
            return slot
        elif not forInsert:
            while self._table[slot] is not self.UNUSED:
                if self._table[slot].key == key:
                    return slot
                else:
                    slot = (slot + step) % M

    # Rebuilds the hash table.
    def _rehash(self):
        # Create a new larger table.
        origTable = self._table
        newSize = len(self._table) * 2 + 1
        self._table = Array(newSize)
        # Modify the size attributes.
        self._count = 0
        self._maxCount = newSize - newSize // 3
        # Add the keys from the original array into the new table
        for entry in origTable:
            if entry is not HashMap.UNUSED and entry is not HashMap.EMPTY:
                slot = self._find_slot(entry.key, True)
                self._table[slot] = entry
                self._count += 1

    # The main hash function for mapping keys to table entries.
    def _hash1(self, key):
        return abs(hash(key)) % len(self._table)

    # The second hash function used with double hashing probes.
    def _hash2(self, key):
        return 1 + abs(hash(key)) % (len(self._table) - 2)

    # Returns an iterator for traversing the keys in the map.
    def __iter__(self):
        return _HashMapIterator(self._table)


class _HashMapIterator:

    def __init__(self, table):
        self._table = table
        self._curr = 0

    def __next__(self):
        if self._curr == len(self._table):
            raise StopIteration()
        key = self._table[self._curr].key
        self._curr += 1
        return key

    def __iter__(self):
        return self
