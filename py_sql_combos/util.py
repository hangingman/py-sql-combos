# -*- coding: utf-8 -*-

def get_table_in_join_clause(table_list, join_clause):
    for tb in table_list:
        if tb in join_clause:
            return tb
