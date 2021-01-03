# Generated from ../cl/PolyLang.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3!")
        buf.write("Z\4\2\t\2\4\3\t\3\3\2\3\2\7\2\t\n\2\f\2\16\2\f\13\2\7")
        buf.write("\2\16\n\2\f\2\16\2\21\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\5\3\33\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\6\3\65\n\3\r\3\16\3\66\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3F\n\3\f\3\16\3I\13\3\3\3")
        buf.write("\3\3\5\3M\n\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3U\n\3\f\3\16")
        buf.write("\3X\13\3\3\3\2\3\4\4\2\4\2\2\2m\2\17\3\2\2\2\4L\3\2\2")
        buf.write("\2\6\n\5\4\3\2\7\t\7\37\2\2\b\7\3\2\2\2\t\f\3\2\2\2\n")
        buf.write("\b\3\2\2\2\n\13\3\2\2\2\13\16\3\2\2\2\f\n\3\2\2\2\r\6")
        buf.write("\3\2\2\2\16\21\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\3")
        buf.write("\3\2\2\2\21\17\3\2\2\2\22\23\b\3\1\2\23\24\7\n\2\2\24")
        buf.write("\25\7\31\2\2\25\26\7\3\2\2\26M\7\35\2\2\27\32\7\13\2\2")
        buf.write("\30\33\5\4\3\2\31\33\7\32\2\2\32\30\3\2\2\2\32\31\3\2")
        buf.write("\2\2\33M\3\2\2\2\34\35\7\f\2\2\35M\5\4\3\20\36\37\7\r")
        buf.write("\2\2\37M\5\4\3\17 !\7\16\2\2!M\5\4\3\16\"#\7\17\2\2#M")
        buf.write("\5\4\3\r$%\7\20\2\2%M\5\4\3\f&\'\7\21\2\2\'(\5\4\3\2(")
        buf.write(")\7\3\2\2)*\5\4\3\13*M\3\2\2\2+,\7\22\2\2,-\5\4\3\2-.")
        buf.write("\7\3\2\2./\5\4\3\n/M\3\2\2\2\60\61\7\23\2\2\61\64\7\32")
        buf.write("\2\2\62\63\7\3\2\2\63\65\5\4\3\2\64\62\3\2\2\2\65\66\3")
        buf.write("\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67M\3\2\2\289\7\27")
        buf.write("\2\29M\5\4\3\b:;\7\30\2\2;M\7\33\2\2<=\7\4\2\2=>\5\4\3")
        buf.write("\2>?\7\5\2\2?M\3\2\2\2@A\7\31\2\2AB\7\24\2\2BM\5\4\3\5")
        buf.write("CG\7\b\2\2DF\7\36\2\2ED\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH")
        buf.write("\3\2\2\2HJ\3\2\2\2IG\3\2\2\2JM\7\t\2\2KM\7\31\2\2L\22")
        buf.write("\3\2\2\2L\27\3\2\2\2L\34\3\2\2\2L\36\3\2\2\2L \3\2\2\2")
        buf.write("L\"\3\2\2\2L$\3\2\2\2L&\3\2\2\2L+\3\2\2\2L\60\3\2\2\2")
        buf.write("L8\3\2\2\2L:\3\2\2\2L<\3\2\2\2L@\3\2\2\2LC\3\2\2\2LK\3")
        buf.write("\2\2\2MV\3\2\2\2NO\f\23\2\2OP\7\25\2\2PU\5\4\3\24QR\f")
        buf.write("\22\2\2RS\7\26\2\2SU\5\4\3\23TN\3\2\2\2TQ\3\2\2\2UX\3")
        buf.write("\2\2\2VT\3\2\2\2VW\3\2\2\2W\5\3\2\2\2XV\3\2\2\2\n\n\17")
        buf.write("\32\66GLTV")
        return buf.getvalue()


class PolyLangParser ( Parser ):

    grammarFileName = "PolyLang.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "'color'", "'print'", "'area'", "'perimeter'", 
                     "'vertices'", "'edges'", "'centroid'", "'equal'", "'inside'", 
                     "'draw'", "':='", "'+'", "'*'", "'#'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "LPARENS", "RPARENS", "LBRACE", 
                      "RBRACE", "LBRACKET", "RBRACKET", "COLOR", "PRINT", 
                      "AREA", "PERIMETER", "VERTICES", "EDGES", "CENTROID", 
                      "EQUAL", "INSIDE", "DRAW", "ASSIGNMENT", "UNION", 
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
    COLOR=8
    PRINT=9
    AREA=10
    PERIMETER=11
    VERTICES=12
    EDGES=13
    CENTROID=14
    EQUAL=15
    INSIDE=16
    DRAW=17
    ASSIGNMENT=18
    UNION=19
    INTERSECTION=20
    BOUNDING_BOX=21
    RANDOM_SAMPLE=22
    IDENTIFIER=23
    STRING=24
    NUMBER=25
    REAL=26
    COLOR_RGB=27
    POINT=28
    NEWLINE=29
    LINE_COMMENT=30
    WS=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PolyLangParser.LPARENS) | (1 << PolyLangParser.LBRACKET) | (1 << PolyLangParser.COLOR) | (1 << PolyLangParser.PRINT) | (1 << PolyLangParser.AREA) | (1 << PolyLangParser.PERIMETER) | (1 << PolyLangParser.VERTICES) | (1 << PolyLangParser.EDGES) | (1 << PolyLangParser.CENTROID) | (1 << PolyLangParser.EQUAL) | (1 << PolyLangParser.INSIDE) | (1 << PolyLangParser.DRAW) | (1 << PolyLangParser.BOUNDING_BOX) | (1 << PolyLangParser.RANDOM_SAMPLE) | (1 << PolyLangParser.IDENTIFIER))) != 0):
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

        def PERIMETER(self):
            return self.getToken(PolyLangParser.PERIMETER, 0)

        def VERTICES(self):
            return self.getToken(PolyLangParser.VERTICES, 0)

        def EDGES(self):
            return self.getToken(PolyLangParser.EDGES, 0)

        def CENTROID(self):
            return self.getToken(PolyLangParser.CENTROID, 0)

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
            self.state = 74
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
                if token in [PolyLangParser.LPARENS, PolyLangParser.LBRACKET, PolyLangParser.COLOR, PolyLangParser.PRINT, PolyLangParser.AREA, PolyLangParser.PERIMETER, PolyLangParser.VERTICES, PolyLangParser.EDGES, PolyLangParser.CENTROID, PolyLangParser.EQUAL, PolyLangParser.INSIDE, PolyLangParser.DRAW, PolyLangParser.BOUNDING_BOX, PolyLangParser.RANDOM_SAMPLE, PolyLangParser.IDENTIFIER]:
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
                self.expr(14)
                pass

            elif la_ == 4:
                self.state = 28
                self.match(PolyLangParser.PERIMETER)
                self.state = 29
                self.expr(13)
                pass

            elif la_ == 5:
                self.state = 30
                self.match(PolyLangParser.VERTICES)
                self.state = 31
                self.expr(12)
                pass

            elif la_ == 6:
                self.state = 32
                self.match(PolyLangParser.EDGES)
                self.state = 33
                self.expr(11)
                pass

            elif la_ == 7:
                self.state = 34
                self.match(PolyLangParser.CENTROID)
                self.state = 35
                self.expr(10)
                pass

            elif la_ == 8:
                self.state = 36
                self.match(PolyLangParser.EQUAL)
                self.state = 37
                self.expr(0)
                self.state = 38
                self.match(PolyLangParser.T__0)
                self.state = 39
                self.expr(9)
                pass

            elif la_ == 9:
                self.state = 41
                self.match(PolyLangParser.INSIDE)
                self.state = 42
                self.expr(0)
                self.state = 43
                self.match(PolyLangParser.T__0)
                self.state = 44
                self.expr(8)
                pass

            elif la_ == 10:
                self.state = 46
                self.match(PolyLangParser.DRAW)
                self.state = 47
                self.match(PolyLangParser.STRING)
                self.state = 50 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 48
                        self.match(PolyLangParser.T__0)
                        self.state = 49
                        self.expr(0)

                    else:
                        raise NoViableAltException(self)
                    self.state = 52 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass

            elif la_ == 11:
                self.state = 54
                self.match(PolyLangParser.BOUNDING_BOX)
                self.state = 55
                self.expr(6)
                pass

            elif la_ == 12:
                self.state = 56
                self.match(PolyLangParser.RANDOM_SAMPLE)
                self.state = 57
                self.match(PolyLangParser.NUMBER)
                pass

            elif la_ == 13:
                self.state = 58
                self.match(PolyLangParser.LPARENS)
                self.state = 59
                self.expr(0)
                self.state = 60
                self.match(PolyLangParser.RPARENS)
                pass

            elif la_ == 14:
                self.state = 62
                self.match(PolyLangParser.IDENTIFIER)
                self.state = 63
                self.match(PolyLangParser.ASSIGNMENT)
                self.state = 64
                self.expr(3)
                pass

            elif la_ == 15:
                self.state = 65
                self.match(PolyLangParser.LBRACKET)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PolyLangParser.POINT:
                    self.state = 66
                    self.match(PolyLangParser.POINT)
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 72
                self.match(PolyLangParser.RBRACKET)
                pass

            elif la_ == 16:
                self.state = 73
                self.match(PolyLangParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 82
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = PolyLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 76
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 77
                        self.match(PolyLangParser.UNION)
                        self.state = 78
                        self.expr(18)
                        pass

                    elif la_ == 2:
                        localctx = PolyLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 79
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 80
                        self.match(PolyLangParser.INTERSECTION)
                        self.state = 81
                        self.expr(17)
                        pass

             
                self.state = 86
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
                return self.precpred(self._ctx, 17)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 16)
         




