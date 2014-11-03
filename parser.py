__author__ = 'deschancesdjomo'

import ply.yacc as yacc
from lexer import Lexer # Import lexer information
import ast

class Parser:

    def __init__(self):
        self.lex = Lexer()
        self.lex.build()
        self.tokens = self.lex.tokens
        self.parser = yacc.yacc(module=self, start = 'Model')

    def parse(self, text, filename=''):
        """ Parses TSML code and returns an AST.

            text:
                A string containing the TSML source code

            filename:
                Name of the file being parsed (for meaningful
                error messages)
        """
        self.lex.filename = filename
        self.lex.reset_lineno()
        return self.parser.parse(
                input=text,
                lexer=self.lex)


    def p_empty(self, p):
        'empty :'
        p[0] = None

    def p_IDList(self, p):
        '''
            IDList : ID
            | IDList COMMA ID
        '''
        if len(p) == 2: # single parameter
            p[0] = ast.ParamList([p[1]])
        else:
            p[1].params.append(p[3])
            elt = ast.ID(p[1])
            p[0] = elt

    def p_PointSeparatedID(self, p):
        '''
            PointSeparatedID : ID
            | PointSeparatedID POINT ID
        '''
        if len(p) == 2: # single parameter
            p[0] = ast.ParamList([p[1]])
        else:
            p[1].params.append(p[3])
            p[0] = p[1]


    def p_EventPath(self, p):
        '''
        EventPath : ID POINT PointSeparatedID
        '''
        eventID = ast.ID(p[1])
        p[0] = ast.EventPath(eventID, p[3])

    def p_EventPathList(self,p):
        '''
            EventPathList : EventPath
            | EventPathList AND EventPath
        '''
        if len(p) == 2: # single synchronization
            p[0] = ast.ParamList([p[1]])
        else:
            p[1].params.append(p[3])
            p[0] = p[1]


    def p_Synchronization(self,p):
        '''
        Synchronization : ID COLON EventPathList
        '''
        eventID = ast.ID(p[1])
        p[0] = ast.Synchronization(eventID, p[3])

    def p_SynchronizationList(self,p):
        '''
            SynchronizationList : Synchronization
            | SynchronizationList Synchronization
        '''
        if len(p) == 2: # single synchronization
            p[0] = ast.ParamList([p[1]])
        else:
            p[1].params.append(p[2])
            p[0] = p[1]

    def p_SynchronizationClause(self, p):
        '''
        SynchronizationClause : SYNCHRONIZATION SynchronizationList
        '''
        p[0] = ast.ObjectDecl(p[1],p[2])


    def p_ClassInstance(self, p):
        '''
        ClassInstance : ID  IDList
        '''
        classID = ast.ID(p[1])
        p[0] =  ast.ClassInstance(classID, p[2])


    def p_ComposedBlockClause(self, t):
        '''
        ComposedBlockClause : ClassInstance
        | Block
        '''

    def p_Transition(self, p):
        '''
        Transition : ID COLON ID ARROW ID
        '''
        eventID = ast.ID(p[1])
        state1 = ast.ID(p[3])
        state2 = ast.ID(p[5])
        p[0] = ast.Transition(eventID, state1, state2)

    def p_TransitionList(self, p):
        '''
            TransitionList : Transition
            | TransitionList Transition
        '''
        if len(p) == 2: # single transition
            p[0] = ast.ParamList([p[1]])
        else:
            p[1].params.append(p[2])
            p[0] = p[1]

    def p_TransitionClause(self, p):
        '''
        TransitionClause : TRANSITION TransitionList
        '''
        print("Je suis dans transition clause")
        p[0] = ast.ObjectDecl(p[1],p[2])


    def p_EventClause(self, p):
        '''
        EventClause : EVENT IDList
        '''
        print("Je suis dans event clause")
        event = ast.ID(p[1])
        eventlist = ast.ParamList(p[2])
        p[0] = ast.ObjectDecl(p[1],p[2])

    def p_StateClause(self, p):
        '''
        StateClause : STATE  IDList
        '''
        print("Je suis dans state clause")
        state = ast.ID(p[1])
        statelist = ast.ParamList(p[2])
        p[0] = ast.ObjectDecl(p[1],p[2])


    def p_BlockBody(self, p):
        '''
        BlockBody : StateClause EventClause TransitionClause
            | ComposedBlockClause  SynchronizationClause
        '''

        p[0] = ast.BasicBlockBody(p[1], p[2], p[3])

    def p_Class(self, p):
        '''
        Class : CLASS ID BlockBody END
        '''
        classID = ast.ID(p[21])
        p[0] = ast.BlockDecl(p[1], classID, p[3])


    def p_ClassList(self, p):
        '''
        ClassList :  Class
        | ClassList Class
        '''

    def p_Block(self, p):
        '''
        Block : BLOCK ID BlockBody END
        '''
        blockID = ast.ID(p[2])
        type = ast.ID(p[1])
        p[0] = ast.BlockDecl(type, blockID, p[3])


    # This is the starting rule due to the start specifier above
    def p_Model(self, p):
        '''
        Model : ClassList Block
        | empty Block
        '''
        if len(p) >= 3:
            p[0] = ast.ModelDecl(p[1], p[2])
        elif len(p) == 2 :
            p[0] = ast.ModelDecl([], p[1])
        else:
            p[0] = ast.ModelDecl([], None)

    # Error rule for syntax errors
    def p_error(self, p):
         if p:
            print("Syntax error at '%s'" % p.value)
            print(p.lineno)
         else:
            print("Syntax error at EOF")



#------------------------------------------------------------------------------
if __name__ == "__main__":
    import time

    t1 = time.time()
    parser = Parser()
    print(time.time() - t1)

    f = open("elevator", "r")
    data = f.read()
    f.close()
    t = parser.parse(text = data)
    t.show()


