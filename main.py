from polygons import * # Class ConvexPolygon, class Point

from antlr4 import *
from cl.TreeVisitor import TreeVisitor # Tree Visitor for this language
from cl.PolyLangLexer import PolyLangLexer
from cl.PolyLangParser import PolyLangParser

if __name__ == "__main__":
    visitor = TreeVisitor()

    #try:
    input_stream = FileStream("examples/clipping.poly")
    lexer = PolyLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PolyLangParser(token_stream)
    tree = parser.prog()
    visitor.visit(tree)
    #except Exception as e:
    #    print("ERROR: Uncaught exception:", e)
