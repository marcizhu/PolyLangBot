# Generated from ../cl/PolyLang.g by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\"")
        buf.write("\\\4\2\t\2\4\3\t\3\3\2\3\2\7\2\t\n\2\f\2\16\2\f\13\2\7")
        buf.write("\2\16\n\2\f\2\16\2\21\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\5\3\33\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\6\3\67\n\3\r\3\16\38\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3H\n\3\f\3\16\3K\13")
        buf.write("\3\3\3\3\3\5\3O\n\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3W\n\3\f")
        buf.write("\3\16\3Z\13\3\3\3\2\3\4\4\2\4\2\2\2p\2\17\3\2\2\2\4N\3")
        buf.write("\2\2\2\6\n\5\4\3\2\7\t\7 \2\2\b\7\3\2\2\2\t\f\3\2\2\2")
        buf.write("\n\b\3\2\2\2\n\13\3\2\2\2\13\16\3\2\2\2\f\n\3\2\2\2\r")
        buf.write("\6\3\2\2\2\16\21\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20")
        buf.write("\3\3\2\2\2\21\17\3\2\2\2\22\23\b\3\1\2\23\24\7\f\2\2\24")
        buf.write("\25\7\32\2\2\25\26\7\3\2\2\26O\7\36\2\2\27\32\7\22\2\2")
        buf.write("\30\33\5\4\3\2\31\33\7\33\2\2\32\30\3\2\2\2\32\31\3\2")
        buf.write("\2\2\33O\3\2\2\2\34\35\7\n\2\2\35O\5\4\3\21\36\37\7\13")
        buf.write("\2\2\37O\5\4\3\20 !\7\16\2\2!O\5\4\3\17\"#\7\21\2\2#O")
        buf.write("\5\4\3\16$%\7\23\2\2%O\5\4\3\r&\'\7\24\2\2\'O\5\4\3\f")
        buf.write("()\7\17\2\2)*\5\4\3\2*+\7\3\2\2+,\5\4\3\13,O\3\2\2\2-")
        buf.write(".\7\20\2\2./\5\4\3\2/\60\7\3\2\2\60\61\5\4\3\n\61O\3\2")
        buf.write("\2\2\62\63\7\r\2\2\63\66\7\33\2\2\64\65\7\3\2\2\65\67")
        buf.write("\5\4\3\2\66\64\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2")
        buf.write("\29O\3\2\2\2:;\7\30\2\2;O\5\4\3\b<=\7\31\2\2=O\7\34\2")
        buf.write("\2>?\7\4\2\2?@\5\4\3\2@A\7\5\2\2AO\3\2\2\2BC\7\32\2\2")
        buf.write("CD\7\25\2\2DO\5\4\3\5EI\7\b\2\2FH\7\37\2\2GF\3\2\2\2H")
        buf.write("K\3\2\2\2IG\3\2\2\2IJ\3\2\2\2JL\3\2\2\2KI\3\2\2\2LO\7")
        buf.write("\t\2\2MO\7\32\2\2N\22\3\2\2\2N\27\3\2\2\2N\34\3\2\2\2")
        buf.write("N\36\3\2\2\2N \3\2\2\2N\"\3\2\2\2N$\3\2\2\2N&\3\2\2\2")
        buf.write("N(\3\2\2\2N-\3\2\2\2N\62\3\2\2\2N:\3\2\2\2N<\3\2\2\2N")
        buf.write(">\3\2\2\2NB\3\2\2\2NE\3\2\2\2NM\3\2\2\2OX\3\2\2\2PQ\f")
        buf.write("\24\2\2QR\7\26\2\2RW\5\4\3\25ST\f\23\2\2TU\7\27\2\2UW")
        buf.write("\5\4\3\24VP\3\2\2\2VS\3\2\2\2WZ\3\2\2\2XV\3\2\2\2XY\3")
        buf.write("\2\2\2Y\5\3\2\2\2ZX\3\2\2\2\n\n\17\328INVX")
        return buf.getvalue()


class PolyLangParser ( Parser ):

    grammarFileName = "PolyLang.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "'area'", "'centroid'", "'color'", "'draw'", 
                     "'edges'", "'equal'", "'inside'", "'perimeter'", "'print'", 
                     "'regular'", "'vertices'", "':='", "'+'", "'*'", "'#'", 
                     "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "LPARENS", "RPARENS", "LBRACE", 
                      "RBRACE", "LBRACKET", "RBRACKET", "AREA", "CENTROID", 
                      "COLOR", "DRAW", "EDGES", "EQUAL", "INSIDE", "PERIMETER", 
                      "PRINT", "REGULAR", "VERTICES", "ASSIGNMENT", "UNION", 
                      "INTERSECTION", "BOUNDING_BOX", "RANDOM_SAMPLE", "IDENTIFIER", 
                      "STRING", "NUMBER", "REAL", "COLOR_RGB", "POINT", 
                      "NEWLINE", "LINE_COMMENT", "WS" ]

    RULE_prog = 0
    RULE_expr = 1

    ruleNames =  [ "prog", "expr" ]

    EOF = Token.EOF
    T__0=1
    LPARENS=2
    RPARENS=3
    LBRACE=4
    RBRACE=5
    LBRACKET=6
    RBRACKET=7
    AREA=8
    CENTROID=9
    COLOR=10
    DRAW=11
    EDGES=12
    EQUAL=13
    INSIDE=14
    PERIMETER=15
    PRINT=16
    REGULAR=17
    VERTICES=18
    ASSIGNMENT=19
    UNION=20
    INTERSECTION=21
    BOUNDING_BOX=22
    RANDOM_SAMPLE=23
    IDENTIFIER=24
    STRING=25
    NUMBER=26
    REAL=27
    COLOR_RGB=28
    POINT=29
    NEWLINE=30
    LINE_COMMENT=31
    WS=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(PolyLangParser.ExprContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PolyLangParser.NEWLINE)
            else:
                return self.getToken(PolyLangParser.NEWLINE, i)

        def getRuleIndex(self):
            return PolyLangParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = PolyLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PolyLangParser.LPARENS) | (1 << PolyLangParser.LBRACKET) | (1 << PolyLangParser.AREA) | (1 << PolyLangParser.CENTROID) | (1 << PolyLangParser.COLOR) | (1 << PolyLangParser.DRAW) | (1 << PolyLangParser.EDGES) | (1 << PolyLangParser.EQUAL) | (1 << PolyLangParser.INSIDE) | (1 << PolyLangParser.PERIMETER) | (1 << PolyLangParser.PRINT) | (1 << PolyLangParser.REGULAR) | (1 << PolyLangParser.VERTICES) | (1 << PolyLangParser.BOUNDING_BOX) | (1 << PolyLangParser.RANDOM_SAMPLE) | (1 << PolyLangParser.IDENTIFIER))) != 0):
                self.state = 4
                self.expr(0)
                self.state = 8
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PolyLangParser.NEWLINE:
                    self.state = 5
                    self.match(PolyLangParser.NEWLINE)
                    self.state = 10
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLOR(self):
            return self.getToken(PolyLangParser.COLOR, 0)

        def IDENTIFIER(self):
            return self.getToken(PolyLangParser.IDENTIFIER, 0)

        def COLOR_RGB(self):
            return self.getToken(PolyLangParser.COLOR_RGB, 0)

        def PRINT(self):
            return self.getToken(PolyLangParser.PRINT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolyLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(PolyLangParser.ExprContext,i)


        def STRING(self):
            return self.getToken(PolyLangParser.STRING, 0)

        def AREA(self):
            return self.getToken(PolyLangParser.AREA, 0)

        def CENTROID(self):
            return self.getToken(PolyLangParser.CENTROID, 0)

        def EDGES(self):
            return self.getToken(PolyLangParser.EDGES, 0)

        def PERIMETER(self):
            return self.getToken(PolyLangParser.PERIMETER, 0)

        def REGULAR(self):
            return self.getToken(PolyLangParser.REGULAR, 0)

        def VERTICES(self):
            return self.getToken(PolyLangParser.VERTICES, 0)

        def EQUAL(self):
            return self.getToken(PolyLangParser.EQUAL, 0)

        def INSIDE(self):
            return self.getToken(PolyLangParser.INSIDE, 0)

        def DRAW(self):
            return self.getToken(PolyLangParser.DRAW, 0)

        def BOUNDING_BOX(self):
            return self.getToken(PolyLangParser.BOUNDING_BOX, 0)

        def RANDOM_SAMPLE(self):
            return self.getToken(PolyLangParser.RANDOM_SAMPLE, 0)

        def NUMBER(self):
            return self.getToken(PolyLangParser.NUMBER, 0)

        def LPARENS(self):
            return self.getToken(PolyLangParser.LPARENS, 0)

        def RPARENS(self):
            return self.getToken(PolyLangParser.RPARENS, 0)

        def ASSIGNMENT(self):
            return self.getToken(PolyLangParser.ASSIGNMENT, 0)

        def LBRACKET(self):
            return self.getToken(PolyLangParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(PolyLangParser.RBRACKET, 0)

        def POINT(self, i:int=None):
            if i is None:
                return self.getTokens(PolyLangParser.POINT)
            else:
                return self.getToken(PolyLangParser.POINT, i)

        def UNION(self):
            return self.getToken(PolyLangParser.UNION, 0)

        def INTERSECTION(self):
            return self.getToken(PolyLangParser.INTERSECTION, 0)

        def getRuleIndex(self):
            return PolyLangParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PolyLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 17
                self.match(PolyLangParser.COLOR)
                self.state = 18
                self.match(PolyLangParser.IDENTIFIER)
                self.state = 19
                self.match(PolyLangParser.T__0)
                self.state = 20
                self.match(PolyLangParser.COLOR_RGB)
                pass

            elif la_ == 2:
                self.state = 21
                self.match(PolyLangParser.PRINT)
                self.state = 24
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [PolyLangParser.LPARENS, PolyLangParser.LBRACKET, PolyLangParser.AREA, PolyLangParser.CENTROID, PolyLangParser.COLOR, PolyLangParser.DRAW, PolyLangParser.EDGES, PolyLangParser.EQUAL, PolyLangParser.INSIDE, PolyLangParser.PERIMETER, PolyLangParser.PRINT, PolyLangParser.REGULAR, PolyLangParser.VERTICES, PolyLangParser.BOUNDING_BOX, PolyLangParser.RANDOM_SAMPLE, PolyLangParser.IDENTIFIER]:
                    self.state = 22
                    self.expr(0)
                    pass
                elif token in [PolyLangParser.STRING]:
                    self.state = 23
                    self.match(PolyLangParser.STRING)
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.state = 26
                self.match(PolyLangParser.AREA)
                self.state = 27
                self.expr(15)
                pass

            elif la_ == 4:
                self.state = 28
                self.match(PolyLangParser.CENTROID)
                self.state = 29
                self.expr(14)
                pass

            elif la_ == 5:
                self.state = 30
                self.match(PolyLangParser.EDGES)
                self.state = 31
                self.expr(13)
                pass

            elif la_ == 6:
                self.state = 32
                self.match(PolyLangParser.PERIMETER)
                self.state = 33
                self.expr(12)
                pass

            elif la_ == 7:
                self.state = 34
                self.match(PolyLangParser.REGULAR)
                self.state = 35
                self.expr(11)
                pass

            elif la_ == 8:
                self.state = 36
                self.match(PolyLangParser.VERTICES)
                self.state = 37
                self.expr(10)
                pass

            elif la_ == 9:
                self.state = 38
                self.match(PolyLangParser.EQUAL)
                self.state = 39
                self.expr(0)
                self.state = 40
                self.match(PolyLangParser.T__0)
                self.state = 41
                self.expr(9)
                pass

            elif la_ == 10:
                self.state = 43
                self.match(PolyLangParser.INSIDE)
                self.state = 44
                self.expr(0)
                self.state = 45
                self.match(PolyLangParser.T__0)
                self.state = 46
                self.expr(8)
                pass

            elif la_ == 11:
                self.state = 48
                self.match(PolyLangParser.DRAW)
                self.state = 49
                self.match(PolyLangParser.STRING)
                self.state = 52 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 50
                        self.match(PolyLangParser.T__0)
                        self.state = 51
                        self.expr(0)

                    else:
                        raise NoViableAltException(self)
                    self.state = 54 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass

            elif la_ == 12:
                self.state = 56
                self.match(PolyLangParser.BOUNDING_BOX)
                self.state = 57
                self.expr(6)
                pass

            elif la_ == 13:
                self.state = 58
                self.match(PolyLangParser.RANDOM_SAMPLE)
                self.state = 59
                self.match(PolyLangParser.NUMBER)
                pass

            elif la_ == 14:
                self.state = 60
                self.match(PolyLangParser.LPARENS)
                self.state = 61
                self.expr(0)
                self.state = 62
                self.match(PolyLangParser.RPARENS)
                pass

            elif la_ == 15:
                self.state = 64
                self.match(PolyLangParser.IDENTIFIER)
                self.state = 65
                self.match(PolyLangParser.ASSIGNMENT)
                self.state = 66
                self.expr(3)
                pass

            elif la_ == 16:
                self.state = 67
                self.match(PolyLangParser.LBRACKET)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PolyLangParser.POINT:
                    self.state = 68
                    self.match(PolyLangParser.POINT)
                    self.state = 73
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 74
                self.match(PolyLangParser.RBRACKET)
                pass

            elif la_ == 17:
                self.state = 75
                self.match(PolyLangParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 86
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 84
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = PolyLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 78
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 79
                        self.match(PolyLangParser.UNION)
                        self.state = 80
                        self.expr(19)
                        pass

                    elif la_ == 2:
                        localctx = PolyLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 81
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 82
                        self.match(PolyLangParser.INTERSECTION)
                        self.state = 83
                        self.expr(18)
                        pass

             
                self.state = 88
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 17)
         




