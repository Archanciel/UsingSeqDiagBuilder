from classc import ClassC

class ClassB:
    def doB(self, p1):
        '''
        This the leaf method of our sequence diagram.
        '''

        c = ClassC()
        c.doC(p1)