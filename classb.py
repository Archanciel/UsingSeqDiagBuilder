from classc import ClassC

class ClassB:
    def doB(self, p1):
        c = ClassC()
        a = 0

        for i in range(3):
            #:seqdiag_loop 3 times
            c.doC1(p1)
            a += 1 # dummy instruction
            c.doC2(p1)
            #:seqdiag_loop  end

        print(a) # another dummy instruction