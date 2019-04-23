#!/usr/bin/env python3

from .constants import *
from .mysql.MySqlLexer import *
from .mysql.MySqlParser import *
import logging.config
from .ast.ast_processor import AstProcessor
from .ast.basic_info_listener import BasicInfoListener


def parse_sql():
    logger = logging.getLogger(__file__)
    ast_info = AstProcessor(
        logging, BasicInfoListener()
    ).execute(SAMPLE_QUERY)

    from pprint import pprint
    pprint(ast_info)
