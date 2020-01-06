import ctypes

class Array:
    def __init__(self,size):
        assert size > 0, "Array size must be greater than zero."
        self.size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        assert index >= 0 and index < len(self), "Array subscript out of range."
        return self._elements[index]

    def __setitem__(self, key, value):
        assert key >= 0 and key < len(self), "Array subscript out of range."
        self._elements[key] = value

    def clear(self,value):
        for i in range(len(self)):
            self._elements[i] = value

    def __repr__(self):
        return "Array({})".format(self._elements)

    def __iter__(self):
        return _ArrayIterator(self._elements)

class _ArrayIterator:
    def __init__(self,theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration


#Implementation of a 2D Array.
class Array2D(Array):
    def __init__(self,numRows,numCols):
        super(Array2D, self).__init__(size=numRows)
        self._theRows = Array(numRows)
        for i in range(numRows):
            self._theRows[i] = Array(numCols)

    def numRows(self):
        return len(self._theRows)

    def numCols(self):
        return len(self._theRows[0])

    def clear(self,value):
        for row in range(self.numRows()):
            super().clear(value)

    def __getitem__(self, ndxtuple):
        assert len(ndxtuple) == 2, "Invalid number of array subscript"
        row = ndxtuple[0]
        col = ndxtuple[1]
        assert row >= 0 and row < self.numRows()\
            and col >= 0 and col < self.numCols(),\
                "Array subscript out of range"
        the1darray = self._theRows[row]
        return the1darray[col]

    def __setitem__(self, ndxtuple, value):
        assert len(ndxtuple) == 2, "Invalid number of array subscript"
        row = ndxtuple[0]
        col = ndxtuple[1]
        assert row >= 0 and row < self.numRows()\
        and col >= 0 and col < self.numCols(),\
            "Array subscript out of range"
        the1darray = self._theRows[row]
        the1darray[col] = value