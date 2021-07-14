from lpparser.LPParser import LPParser
from lpparser.LPLexer import LPLexer
from lpparser.LPModelListener import LPModelListener
from lpparser.TempModel import TempModel
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker


def read(f) -> TempModel:
    lp_txt = FileStream(f)

    lexer = LPLexer(lp_txt)
    stream = CommonTokenStream(lexer)
    parser = LPParser(stream)

    tree = parser.prog()

    model_listener = LPModelListener()

    walker = ParseTreeWalker()
    walker.walk(model_listener, tree)

    return model_listener.tmp_model
