__author__ = 'deschancesdjomo'
##################################################
#
# Lexer
#
####################################################


reserved = {
   'block' : 'BLOCK',
   'class' : 'CLASS',
   'event' : 'EVENT',
   'end' : 'END',
   'state':'STATE',
   'transition':'TRANSITION',
   'synchronization': 'SYNCHRONIZATION',
}

tokens = ['ID', 'ARROW', 'COLON', 'POINT', 'COMMA', 'AND'] + list(reserved.values())


#Tokens

t_ARROW = r'->'
t_COLON = r':'
t_POINT = r'\.'
t_COMMA = r','
t_AND = r'&'


# Ignored characters
t_ignore = " \t"

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()
"""
lex.input("class Door " \
       "state open, close " \
       "event opening, closing " \
       "transition " \
       "opening: close -> open " \
       "closing: open -> close " \
       "end")
while True:
    tok = lex.token()
    if not tok: break
    print(tok)

"""
