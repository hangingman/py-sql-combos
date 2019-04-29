from mysql.MySqlParserListener import MySqlParserListener
from mysql.MySqlParser import MySqlParser


class BasicInfoListener(MySqlParser):

    def __init__(self):
        self.ast_info = {
            'root': "",
            'sql_statements': [],
            'join_parts': [],
            'from_clause': "",
            'select_elements': []
        }


    # クエリ全体
    def enterRoot(self, ctx:MySqlParser.RootContext):
        self.ast_info['root'] = ctx.getText()

    def exitRoot(self, ctx:MySqlParser.RootContext):
        pass

    # ; までのクエリ
    def enterSqlStatements(self, ctx:MySqlParser.SqlStatementsContext):
        self.ast_info['sql_statements'].append(ctx.getText())

    def exitSqlStatements(self, ctx:MySqlParser.SqlStatementsContext):
        pass

    # select句のすべての要素
    def enterSelectElements(self, ctx:MySqlParser.SelectElementsContext):
        self.ast_info['select_elements'].append(ctx.getText())

    def exitSelectElements(self, ctx:MySqlParser.SqlStatementsContext):
        pass

    def enterFromClause(self, ctx:MySqlParser.FromClauseContext):
        self.ast_info['from_clause'] = ctx.getText()

    def enterJoinPart(self, ctx:MySqlParser.JoinPartContext):
        self.ast_info['join_parts'].append(ctx.getText())

    def exitJoinPart(self, ctx:MySqlParser.JoinPartContext):
        pass


    def enterEveryRule(self, ctx):
        pass


    def exitEveryRule(self, ctx):
        pass


    def visitTerminal(self, ctx):
        pass
