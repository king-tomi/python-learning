class Adder:
    def add(self,x,y):
        print("Not implemented")


class ListAdder(Adder):
    def add(self,x,y):
         self.x = list(x)
         self.y = list(y)
         self.x.extend(self.y)
         self._display(self.x)

    @staticmethod
    def _display(x):
        print(x)

class DictAdder(Adder):
    def add(self,x,y):
        self.x = dict(x)
        self.y = dict(y)
        for k,v in self.x.items():
            self.y.get(k)
        self._display(self.y)

    @staticmethod
    def _display(x):
        print(x)