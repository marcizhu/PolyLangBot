# Generated from ../cl/PolyLang.g by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PolyLangParser import PolyLangParser
else:
    from PolyLangParser import PolyLangParser

# This class defines a complete generic visitor for a parse tree produced by PolyLangParser.

class PolyLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PolyLangParser#prog.
    def visitProg(self, ctx:PolyLangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolyLangParser#expr.
    def visitExpr(self, ctx:PolyLangParser.ExprContext):
        return self.visitChildren(ctx)



del PolyLangParser