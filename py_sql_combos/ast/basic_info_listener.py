from mysql.MySqlParserListener import MySqlParserListener
from mysql.MySqlParser import MySqlParser


class BasicInfoListener(MySqlParser):

    def __init__(self):
        self.ast_info = {
            'root': "",
            'sql_statements': [],
        }


    def enterRoot(self, ctx:MySqlParser.RootContext):
        #print("Enter root")
        #print("  " + ctx.getText())
        self.ast_info['root'] = ctx.getText()


    def exitRoot(self, ctx:MySqlParser.RootContext):
        #print("Exit root")
        pass


    def enterSqlStatements(self, ctx:MySqlParser.SqlStatementsContext):
        #print("  Enter sql_statements")
        #print("    " + ctx.getText())
        self.ast_info['sql_statements'].append(ctx.getText())


    def exitSqlStatements(self, ctx:MySqlParser.SqlStatementsContext):
        #print("  Exit sql_statements")
        pass


    def enterEveryRule(self, ctx):
        pass

    def exitEveryRule(self, ctx):
        pass

    def visitTerminal(self, ctx):
        pass
