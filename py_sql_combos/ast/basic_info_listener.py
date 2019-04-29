from mysql.MySqlParserListener import MySqlParserListener
from mysql.MySqlParser import MySqlParser


class BasicInfoListener(MySqlParser):

    def __init__(self):
        self.call_methods = []

    def enterRoot(self, ctx:MySqlParser.RootContext):
        print("**1")
        print(ctx.getText())
        print("***")

    def enterSqlStatement(self, ctx:MySqlParser.SqlStatementContext):
        print("**2")
        print(ctx.getText())
        print("***")

    def enterSqlStatements(self, ctx:MySqlParser.SqlStatementsContext):
        print("**3")
        print(ctx.getText())
        print("***")

    def enterEveryRule(self, ctx):
        print("enter every rule")
