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

    # JOINの条件を全て取得
    def enterOuterJoin(self, ctx:MySqlParser.OuterJoinContext):
        self.ast_info['join_parts'].append(ctx.getText())

    def exitOuterJoin(self, ctx:MySqlParser.JoinPartContext):
        pass

    # Joinは以下の４つある
    # InnerJoinContext
    # StraightJoinContext
    # OuterJoinContext
    # NaturalJoinContext

    # 以下、動作に必要なメソッド
    def enterEveryRule(self, ctx):
        pass


    def exitEveryRule(self, ctx):
        pass


    def visitTerminal(self, ctx):
        pass
