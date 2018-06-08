import nltk
import re
import sys

import autoindent


reserved_words = {
    "program": "PROGRAM",
    "begin": "BEGIN",
    "end": "END",
    "const": "CONST",
    "type": "TYPE",
    "var": "VAR",
    ".": "DOT",
    "..": "DOTDOT",
    ";": "SEMICOLON",
    ":": "COLON",
    ",": "COMMA",
    "=": "EQUAL",
    "<>": "DIFFERENT",
    "<": "LT",
    ">": "GT",
    "<=": "LTE",
    ">=": "GTE",
    ":=": "ASSIGN",
    "+": "ADD",
    "-": "SUB",
    "or": "OR",
    "*": "MUL",
    "/": "RDIV",
    "div": "DIV",
    "mod": "MOD",
    "and": "AND",
    "not": "NOT",
    "while": "WHILE",
    "do": "DO",
    "repeat": "REPEAT",
    "until": "UNTIL",
    "for": "FOR",
    "to": "TO",
    "downto": "DOWNTO",
    "if": "IF",
    "then": "THEN",
    "else": "ELSE",
    ")": "CPAR",
    "(": "OPAR",
    "]": "CSQRBRA",
    "[": "OSQRBRA",
    "array": "ARRAY",
    "of": "OF"
}


def tokenize(text):
    return re.findall(r"(?:[^\s\.;=<>:\+\*\-\,\/\[\]\(\)]+|;|\.{1,2}|<>|<=|>=|:=|=|<|>|\*|\+|\-|\,|\/|\[|\]|\(|\)|:)", text, flags=re.I)

def map_to_terminal(token):
    lw_terminal = token.lower()
    if lw_terminal in reserved_words:
        return reserved_words[lw_terminal]
    elif re.match(r"\d+$", lw_terminal):
        return "NUMBER"
    else:
        return "IDENT"

def load_gramar():
    with open('grammar.txt', 'r') as f:
        return nltk.CFG.fromstring(f.read())


if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = open(archivo_entrada, 'r')
    s = f.read()
    f.close()
    lista = [map_to_terminal(token) for token in tokenize(s)]
    print (lista)
    parser = nltk.ChartParser(load_gramar())
    reconoce = False;
    tree = [t for t in parser.parse(lista)][:1]
   
    f = open(archivo_salida, 'w')
    if tree:
        print(tree)
        f.write(autoindent.print_indented(tree[0]))
    else:
        f.write("SINTAXIS INCORRECTA")
    f.close()
