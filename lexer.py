__author__ = 'deschancesdjomo'
##################################################
#
# Lexer
#
####################################################
import re
from ply import lex
from ply.lex import TOKEN

class Lexer(object):

     def __init__(self):
        """ Create a new Lexer.

            error_func:
                An error function. Will be called with an error
                message, line and column as arguments, in case of
                an error during lexing.
        """
        self.filename = ''

        # Keeps track of the last token returned from self.token()
        self.last_token = None


     def build(self, **kwargs):
        """ Builds the lexer from the specification. Must be
            called after the lexer object is created.

            This method exists separately, because the PLY
            manual warns against calling lex.lex inside
            __init__
        """
        self.lexer = lex.lex(object=self, **kwargs)

     def reset_lineno(self):
        """ Resets the internal line number counter of the lexer.
        """
        self.lexer.lineno = 1

     def input(self, text):
        self.lexer.input(text)

     def token(self):
        self.last_token = self.lexer.token()
        return self.last_token

     def find_tok_column(self, token):
        """ Find the column of the token in its line.
        """
        last_cr = self.lexer.lexdata.rfind('\n', 0, token.lexpos)
        return token.lexpos - last_cr



     ##
     ## Reserved keywords
     ##
     keywords = {
       'block' : 'BLOCK',
       'class' : 'CLASS',
       'event' : 'EVENT',
       'end' : 'END',
       'state':'STATE',
       'transition':'TRANSITION',
       'synchronization': 'SYNCHRONIZATION',
     }

     keyword_map = {}
     for keyword in keywords:
        keyword_map[keyword.lower()] = keyword

     ##
     ## All the tokens recognized by the lexer
     ##
     tokens = ['ID',
              'ARROW',
              'COLON',
              'POINT',
              'COMMA',
              'AND'] + list(keywords.values())


     #Tokens
     t_ARROW = r'->'
     t_COLON = r':'
     t_POINT = r'\.'
     t_COMMA = r','
     t_AND = r'&'


    ##
    ## Regexes for use in tokens
    ##
    ##

     # Ignored characters
     t_ignore = " \t"

     identifier = r'[a-zA-Z_][a-zA-Z_0-9]*'

     @TOKEN(identifier)
     def t_ID(self, t):
        t.type = self.keywords.get(t.value,'ID')    # Check for reserved words
        return t

     def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

     def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

