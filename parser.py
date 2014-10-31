__author__ = 'deschancesdjomo'

import ply.yacc as yacc
import lexer # Import lexer information

tokens = lexer.tokens # Need token list

# dictionary of names
names = { }

def p_empty(p):
    'empty :'
    pass

def p_IDList(t):
    '''
        IDList : COMMA ID
        | empty
    '''

def p_PointSeparatedID(t):
    '''
        PointSeparatedID : POINT ID
        | empty
    '''


def p_EventIdentifier(t):
    '''
    EventIdentifier : ID
    '''


def p_EventPath(t):
    '''
    EventPath : ID PointSeparatedID
    '''

def p_AndSeparatedEventPath(t):
    '''
        AndSeparatedEventPath : AND EventPath
        | empty
    '''

def p_MacroEventDefinition(t):
    '''
    MacroEventDefinition : EventIdentifier COLON EventPath AndSeparatedEventPath
    '''

def p_Synchronization(t):
    '''
    Synchronization : MacroEventDefinition
    '''


def p_SynchronizationList(t):
    '''
        SynchronizationList : Synchronization SynchronizationList
        | empty
    '''

def p_SynchronizationClause(t):
    '''
    SynchronizationClause : SYNCHRONIZATION Synchronization SynchronizationList
    '''

def p_ClassIdentifier(t):
    '''
    ClassIdentifier : ID
    '''

def p_ClassInstance(t):
    '''
    ClassInstance : ClassIdentifier ID IDList
    '''

def p_ComposedBlockClause(t):
    '''
    ComposedBlockClause : ClassInstance
    | Block
    '''

def p_StateIdentifier(t):
    '''
    StateIdentifier : ID
    '''

def p_Transition(t):
    '''
    Transition : EventIdentifier COLON StateIdentifier ARROW StateIdentifier TransitionList
    '''

def p_TransitionList(t):
    '''
        TransitionList : Transition
        | empty
    '''

def p_TransitionClause(t):
    '''
    TransitionClause : TRANSITION Transition
    '''

def p_EventClause(t):
    '''
    EventClause : EVENT ID IDList
    '''

def p_StateClause(t):
    '''
    StateClause : STATE ID IDList
    '''


def p_InternalBlockBody(t):
    '''
    InternalBlockBody : ComposedBlockClause EventClause SynchronizationClause
    '''

def p_BasicBlockBody(t):
    '''
    BasicBlockBody : StateClause EventClause TransitionClause
    '''


def p_BlockBody(t):
    '''
    BlockBody : BasicBlockBody
        | InternalBlockBody
    '''


def p_Class(t):
    '''
    Class : CLASS ID BlockBody END
    '''


def p_ClassList(t):
    '''
    ClassList : Class ClassList
    | empty
    '''
    print(t[1])

def p_Block(t):
    '''
    Block : BLOCK ID BlockBody END
    '''
    print(t[2])

# This is the starting rule due to the start specifier above
def p_Model(t):
    '''
    Model : ClassList Block
    | empty
    '''
    print(t[1])

# Error rule for syntax errors
def p_error(p):
    print ("Syntax error at token", p.type)
    print ("Syntax error at line", p.lineno)
    # Just discard the token and tell the parser it's okay.
    yacc.token()

yacc.yacc(start = 'Model')

f = open("elevator", "r")
data = f.read()
f.close()
yacc.parse(data,tracking=True)


