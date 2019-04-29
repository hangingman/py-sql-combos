from mysql.MySqlParserListener import MySqlParserListener
from mysql.MySqlParser import MySqlParser


class BasicInfoListener(MySqlParser):

    def __init__(self):
        self.call_methods = []

    def enterRoot(self, ctx:MySqlParser.RootContext):
        print("**1")
        print(ctx.getText())
        print(ctx.toStringTree())
        print("***")

    def enterEveryRule(self, ctx):
        print("enter every rule")
