from ArrayStack import ArrayStack
if  __name__ == "__main__":
    def is_matched(expr):
        lefty = '({['
        righty = ')}]'
        s = ArrayStack()
        for c in expr:
            if c in  lefty:
                s.push(c)
            elif c in righty:
                if s.is_empty():
                    return False
                if righty.index(c) != lefty.index(s.pop()):
                    return False
        return s.is_empty()

    print(is_matched('()[]'))