
from nltk import Tree

reserved_words = {
    "PROGRAM": "program ",
    "BEGIN": "begin\n",
    "END": "\nend",
    "CONST": "const\n",
    "TYPE": "type",
    "VAR": "var\n",
    "DOT": ".",
    "DOTDOT": "..",
    "SEMICOLON": ";\n", 
    "COLON": ":", 
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
    "WHILE": "while\n",
    "DO": "do\n",
    "REPEAT": "repeat ",
    "UNTIL": "until ",
    "FOR": "for " ,
    "TO": "to ",
    "DOWNTO": "downto ",
    "IF": "if ",
    "THEN": " then\n",
    "ELSE": "\nelse\n" ,
    "CPAR": ")", 
    "OPAR": "(", 
    "CSQRBRA": "]", 
    "OSQRBRA": "[", 
    "ARRAY": "array",
    "OF": "of",
    "NUMBER": "NUM"

}
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
	else:
		return token

#    elif re.match(r"\d+$", lw_terminal):
#        return "NUMBER"
#    else:
#        return "IDENT"

#tab = ''
def print_indented(tree):
  """
  Retorna el programa contenido en tree indentado en una string.
  """
  t = ''
  for node in tree:
    tab = ''
    for i in range(1, depth(node)):
      tab = tab +' '
    if type(node) is Tree:
      t = t + print_indented(node)
    else:
      t = t +  map_to_terminal(node)

  return t    
  
  
  
  

