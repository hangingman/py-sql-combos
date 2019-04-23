#!/usr/bin/env python3

from .constants import *
from .mysql.MySqlLexer import *
from .mysql.MySqlParser import *
from antlr4 import *
from antlr4.tree.Trees import Trees


def parse_sql():
    print("hello")
    lexer = MySqlLexer(SAMPLE_QUERY)
    stream = CommonTokenStream(lexer)
    parser = MySqlParser(stream)

