from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from ..mysql.MySqlLexer import MySqlLexer
from ..mysql.MySqlParser import MySqlParser
from pprint import pformat


class AstProcessor:

    def __init__(self, logging, listener):
        self.logging = logging
        self.logger = logging.getLogger(self.__class__.__name__)
        self.listener = listener

    def execute(self, input_source):
        parser = MySqlParser(CommonTokenStream(MySqlLexer(InputStream(input_source))))
        walker = ParseTreeWalker()
        walker.walk(self.listener, parser)
        self.logger.debug('Display all data extracted by AST. \n' + pformat(self.listener.ast_info, width=160))
        return self.listener.ast_info
