
class SymmetricMatrix:

    def __init__(self, size):
        self._data = {}
        self._size = size

    def _hash(self, indexes):
        if indexes[0] > indexes[1]:
            indexes = [indexes[1], indexes[0]]
        return indexes[0]*self._size + indexes[1]

    def __getitem__(self, indexes):
        hashed = self._hash(indexes)
        return self._data[hashed]

    def __setitem__(self, indexes, value):
        hashed = self._hash(indexes)
        self._data[hashed] = value

    def __str__(self):
        mtx_str = ""
        for i in range(self._size):
            for j in range(self._size):
                mtx_str += str(self[i, j]) + " ; "
            mtx_str += "\n"
        return mtx_str

    def __add__(self, other):
        keys = self._data.keys()
        result = SymmetricMatrix(other._size)
        for k in keys:
            result._data[k] = self._data[k] + other._data[k]
        return result


if __name__ == '__main__':
    mySymmatrix1 = SymmetricMatrix(3)
    mySymmatrix2 = SymmetricMatrix(3)
    theResult = SymmetricMatrix(3)
    mySymmatrix1[0, 0] = 1
    mySymmatrix1[0, 1] = 2
    mySymmatrix1[0, 2] = 3
    mySymmatrix1[1, 1] = 2
    mySymmatrix1[1, 2] = 3
    mySymmatrix1[2, 2] = 4

    mySymmatrix2[0, 0] = 1
    mySymmatrix2[0, 1] = 2
    mySymmatrix2[0, 2] = 3
    mySymmatrix2[1, 1] = 2
    mySymmatrix2[1, 2] = 3
    mySymmatrix2[2, 2] = 4

    theResult = mySymmatrix1 + mySymmatrix2
    print(mySymmatrix1)
    print(mySymmatrix2)
    print(theResult)
