

class Protected:
    def __init__(self):
        self._protectedVar = 0

obj = Protected()
obj._protectedVar = 50
print(obj._protectedVar)


class Protected1:
    def __init__(self):
        self.__privateVar = 30

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected1()
obj.getPrivate()
obj.setPrivate(9)
obj.getPrivate()
