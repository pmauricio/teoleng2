
from nltk import Tree
import re
import sys
import os
import glob

reserved_words = {
    "PROGRAM": "program ",
    "BEGIN": "begin\n",
    "END": "end",
    "CONST": "const\n  ",
    "TYPE": "type\n  ",
    "VAR": "var\n  ",
    "DOT": ".",
    "DOTDOT": "..",
    "SEMICOLON": ";\n", 
    "COLON": " : ", 
    "COMMA": ", ", 
    "EQUAL": " = ", 
    "DIFFERENT": " <> ",
    "LT": " < ",
    "GT": " > ",
    "LTE": " <= ",
    "GTE": " >= ",
    "ASSIGN": " := ",
    "ADD": " + ",
    "SUB": " - ",
    "OR": " or ",
    "MUL": " * ",
    "RDIV": " / ",
    "DIV": " div ",
    "MOD": " mod ",
    "AND": " and ",
    "NOT": " not ",
    "WHILE": "while ",
    "DO": " do\n",
    "REPEAT": "repeat ",
    "UNTIL": "until ",
    "FOR": "for " ,
    "TO": " to ",
    "DOWNTO": "downto ",
    "IF": "if ",
    "THEN": " then\n",
    "ELSE": "else\n" ,
    "CPAR": ")", 
    "OPAR": "(", 
    "CSQRBRA": "]", 
    "OSQRBRA": "[", 
    "ARRAY": "array",
    "OF": "of",
    "NUMBER": "NUM"


}

id = 0
cantBegin = 0

def identar(i):
  r = ''
  for id in range(i):
    r = r + '  '
  return r
  
  
def depth(t):
  d=0
  for node in t:
    if type(node) is Tree:
      d = max(depth(node)+1,d)
    else:
      d = max(1,d)
  

  return d	

def map_to_terminal(token):
    if token in reserved_words:
        return reserved_words[token]
    elif re.match(r"\d+$", token):
        return "NUMBER"
    else:
        return "IDENT"
		
def print_indented(tree):
  """
  Retorna el programa contenido en tree indentado en una string.
  """
  t=''
  global id
  global cantBegin
  global beginInterno
  for node in tree:
    if type(node) is Tree:
      if (node.label() == 'constants_aux') or (node.label() == 'types_aux') or (node.label() == 'variables_aux'):
        if (depth(node) == 0 ):
          t = t + print_indented(node)
        else:
          t = t + '  '+ print_indented(node)
      elif (node.label() == 'statement'):
        if (depth(node) == 0 ):
          t = t + print_indented(node)
        else:
          t = t + identar(id) + print_indented(node)
          if (id > 0) and ((0 < cantBegin < 2) or not beginInterno):
            id = id - 1
            beginInterno = True
      elif (node.label() == 'statementSequence_aux'):
        if (depth(node) == 0 ):
          id = id - 1
        t = t + print_indented(node)
      else:
        t = t + print_indented(node)
    else:
      if (node == 'BEGIN'):
        if (cantBegin > 0 ):
          beginInterno = True
          id = id + 1
        cantBegin =cantBegin + 1
      if (node == 'END'):
        t = t + '\n' + identar(id)
        id = id - 1
        cantBegin = cantBegin - 1
      if (node == 'DO') or  (node == 'REPEAT') or (node == 'THEN'):
        beginInterno = False	
        id = id + 1	    
      if (node == 'ELSE'):
        beginInterno = False	
        t = t + '\n' + identar(id)
        id = id + 1
      t = t +  map_to_terminal(node)        
  return t
  
  
  
  

