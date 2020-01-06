class Matrix:

    def __init__(self,row,column):
        self.row = row
        self.column = column
        self.items = [[0]*self.column for j in range(self.row)]


    def __len__(self):
        return self.row

    def is_empty(self):
        return self.row == 0

    def __str__(self):
        for i in range(self.row):
            for j in range(self.column):
                print(str(self.items[i][j]) + " ")
            print()


    def fill(self):                                     #this allows the user to fill the matrix with entries
        print("Enter the entries as they appear")
        for i in range(self.row):
            for j in range(self.column):
                num = int(input(""))
                self.items[i][j] = num

    def dimension(self):
        return self.row,self.column

    def add(self,arr):
        """This is an add method where the user can add two matrices together as long as the
            dimensions agree"""
        new_mat = [[0]*self.column for k in range(self.row)]
        if len(arr) == self.row and len(arr[0]) == self.column:
            for i in range(self.row):
                for j in range(self.column):
                   new_mat[i][j] = self.items[i][j] + arr[i][j]
            return new_mat
        else:
            return False

    def multiply(self,arr):
        product = [[0]* self.row for i in range(len(arr))]
        if self.column == len(arr):
            for i in range(self.row):
                for j in range(self.column):
                    product[i][j] += self.items[i][j] * arr[j][i]
            return product
        else:
            raise ValueError('Matrices do not conform')

    def is_symmetric(self):
        res = [[None] * self.row for k in  range(self.column)]
        for i in range(self.column):
            for j in range(self.row):
                res.append(self.items[j][i])
        return res == self.items