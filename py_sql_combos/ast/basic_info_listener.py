from mysql.MySqlParserListener import MySqlParserListener
from mysql.MySqlParser import MySqlParser


class BasicInfoListener(MySqlParser):

    def __init__(self):
        self.call_methods = []
        self.root = ""

    def enterRoot(self, ctx:MySqlParser.RootContext):
        print("enter root")
        print("  " + ctx.getText())
        self.root = ctx.getText()
        print("exit root")

    def enterEveryRule(self, ctx):
        print("enter every rule")
