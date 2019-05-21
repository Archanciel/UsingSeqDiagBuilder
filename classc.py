from seqdiagbuilder import SeqDiagBuilder

class ClassC:
    def doC(self, p1):
        '''
        This the leaf method of our sequence diagram.
        '''

        # The next instruction causes SeqDiagBuilder to record the
        # whole control flow which conducted to call the present method.
        SeqDiagBuilder.recordFlow()
