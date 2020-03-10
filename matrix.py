class Matrix:
    """A Matrix class for addition, multiplication and subtraction of two dimensional matrices

       _attr: [row,column,item]

       Author: Ayodabo Tomisin

       Date Modified: 09 - 03 - 2020
    """

    def __init__(self,row,column):
        self._row = row
        self._column = column
        self._items = [[0]*self._column for _ in range(self._row)]


    def __len__(self):
        return self._row

    def is_empty(self):
        return self._row == 0

    def __getitem__(self,i,j):
        if not 0 <=i<=self._row and 0<=j<=self._column:
            raise IndexError("Index out of range")
        return self._items[i][j]
    
    def __getitem__(self, item):
        if not 0 <= item <= self._row:
            raise IndexError
        return self._items[item]

    def __setitem__(self,i,j,value):
        if not 0 <= i <= self._row and 0 <= j <= self._column:
            raise IndexError
        self._items[i][j] = value
        
    def __setitem__(self, key, value):
        if not 0 <= key <= self._row:
            raise IndexError
        if not isinstance(value,list):
            raise ValueError
        self._items[key] = value

    def __str__(self):
        matrix = ""
        for i in range(self._row):
            for j in range(self._column):
                matrix += "".join(str(self._items[i][j]))
            matrix += "\n"
        return matrix


    def fill(self):                                     #this allows the user to fill the matrix with entries
        print("Enter the entries as they appear")
        for i in range(self._row):
            for j in range(self._column):
                num = int(input(""))
                self._items[i][j] = num

    def dimension(self):
        return self._row,self._column

    def add(self,arr):
        """This is an add method where the user can add two matrices together as long as the
            dimensions agree"""
        new_mat = [[0]*self._column for k in range(self._row)]
        if len(arr) == self._row and len(arr[0]) == self._column:
            for i in range(self._row):
                for j in range(self._column):
                   new_mat[i][j] = self._items[i][j] + arr[i][j]
            return new_mat
        else:
            return False

    def multiply(self,arr):
        product = [[0]* self._row for i in range(len(arr))]
        if self._column == len(arr):
            for i in range(self._row):
                for j in range(self._column):
                    product[i][j] += self._items[i][j] * arr[j][i]
            return product
        else:
            raise ValueError('Matrices do not conform')

    def is_symmetric(self):
        res = [[None] * self._row for k in  range(self._column)]
        for i in range(self._column):
            for j in range(self._row):
                res.append(self._items[j][i])
        return res == self._items