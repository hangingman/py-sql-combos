from mysql.MySqlParserListener import MySqlParserListener
from mysql.MySqlParser import MySqlParser


class BasicInfoListener(MySqlParser):

    def __init__(self):
        self.call_methods = []
        self.ast_info = {
            'simpleSelect': ''
        }

    def enterSimpleSelect(self, ctx:MySqlParser.SimpleSelectContext):
        self.ast_info['simpleSelect'] = ctx.qualifiedName().getText()
