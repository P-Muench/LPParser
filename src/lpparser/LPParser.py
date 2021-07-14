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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("\u011d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\2\3\2\5\2\61")
        buf.write("\n\2\3\2\5\2\64\n\2\3\2\5\2\67\n\2\3\2\5\2:\n\2\5\2<\n")
        buf.write("\2\3\2\3\2\3\3\3\3\3\4\7\4C\n\4\f\4\16\4F\13\4\3\4\3\4")
        buf.write("\6\4J\n\4\r\4\16\4K\3\4\3\4\5\4P\n\4\3\5\3\5\6\5T\n\5")
        buf.write("\r\5\16\5U\3\5\6\5Y\n\5\r\5\16\5Z\3\5\5\5^\n\5\3\6\3\6")
        buf.write("\6\6b\n\6\r\6\16\6c\3\6\6\6g\n\6\r\6\16\6h\3\6\5\6l\n")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\3\t\6\tt\n\t\r\t\16\tu\3\t\6\t")
        buf.write("y\n\t\r\t\16\tz\6\t}\n\t\r\t\16\t~\3\t\5\t\u0082\n\t\3")
        buf.write("\n\3\n\6\n\u0086\n\n\r\n\16\n\u0087\3\n\6\n\u008b\n\n")
        buf.write("\r\n\16\n\u008c\6\n\u008f\n\n\r\n\16\n\u0090\3\n\5\n\u0094")
        buf.write("\n\n\3\13\5\13\u0097\n\13\3\13\7\13\u009a\n\13\f\13\16")
        buf.write("\13\u009d\13\13\3\13\3\13\7\13\u00a1\n\13\f\13\16\13\u00a4")
        buf.write("\13\13\3\13\3\13\7\13\u00a8\n\13\f\13\16\13\u00ab\13\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\r\5\r\u00b3\n\r\3\r\3\r\7\r\u00b7")
        buf.write("\n\r\f\r\16\r\u00ba\13\r\3\r\3\r\7\r\u00be\n\r\f\r\16")
        buf.write("\r\u00c1\13\r\3\r\3\r\3\16\5\16\u00c6\n\16\3\16\3\16\3")
        buf.write("\17\3\17\7\17\u00cc\n\17\f\17\16\17\u00cf\13\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\7\20\u00d6\n\20\f\20\16\20\u00d9\13")
        buf.write("\20\3\20\3\20\5\20\u00dd\n\20\3\21\3\21\3\21\5\21\u00e2")
        buf.write("\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00ec")
        buf.write("\n\22\3\23\3\23\7\23\u00f0\n\23\f\23\16\23\u00f3\13\23")
        buf.write("\3\23\3\23\7\23\u00f7\n\23\f\23\16\23\u00fa\13\23\3\23")
        buf.write("\3\23\7\23\u00fe\n\23\f\23\16\23\u0101\13\23\3\23\3\23")
        buf.write("\7\23\u0105\n\23\f\23\16\23\u0108\13\23\3\23\3\23\3\24")
        buf.write("\3\24\7\24\u010e\n\24\f\24\16\24\u0111\13\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u0119\n\25\3\26\3\26\3\26\r")
        buf.write("\u009b\u00a2\u00a9\u00b8\u00bf\u00d7\u00f1\u00f8\u00ff")
        buf.write("\u0106\u010f\2\27\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*\2\5\3\2\6\7\3\2\21\22\3\2\23\25\2\u0133\2,")
        buf.write("\3\2\2\2\4?\3\2\2\2\6D\3\2\2\2\bQ\3\2\2\2\n_\3\2\2\2\f")
        buf.write("m\3\2\2\2\16o\3\2\2\2\20q\3\2\2\2\22\u0083\3\2\2\2\24")
        buf.write("\u0096\3\2\2\2\26\u00ae\3\2\2\2\30\u00b2\3\2\2\2\32\u00c5")
        buf.write("\3\2\2\2\34\u00c9\3\2\2\2\36\u00dc\3\2\2\2 \u00e1\3\2")
        buf.write("\2\2\"\u00eb\3\2\2\2$\u00ed\3\2\2\2&\u010b\3\2\2\2(\u0118")
        buf.write("\3\2\2\2*\u011a\3\2\2\2,-\5\6\4\2-.\5\b\5\2.;\5\n\6\2")
        buf.write("/\61\5\22\n\2\60/\3\2\2\2\60\61\3\2\2\2\61\63\3\2\2\2")
        buf.write("\62\64\5\20\t\2\63\62\3\2\2\2\63\64\3\2\2\2\64<\3\2\2")
        buf.write("\2\65\67\5\20\t\2\66\65\3\2\2\2\66\67\3\2\2\2\679\3\2")
        buf.write("\2\28:\5\22\n\298\3\2\2\29:\3\2\2\2:<\3\2\2\2;\60\3\2")
        buf.write("\2\2;\66\3\2\2\2<=\3\2\2\2=>\5\34\17\2>\3\3\2\2\2?@\t")
        buf.write("\2\2\2@\5\3\2\2\2AC\7\5\2\2BA\3\2\2\2CF\3\2\2\2DB\3\2")
        buf.write("\2\2DE\3\2\2\2EG\3\2\2\2FD\3\2\2\2GI\5\4\3\2HJ\7\17\2")
        buf.write("\2IH\3\2\2\2JK\3\2\2\2KI\3\2\2\2KL\3\2\2\2LM\3\2\2\2M")
        buf.write("O\5\32\16\2NP\7\17\2\2ON\3\2\2\2OP\3\2\2\2P\7\3\2\2\2")
        buf.write("QX\7\13\2\2RT\7\17\2\2SR\3\2\2\2TU\3\2\2\2US\3\2\2\2U")
        buf.write("V\3\2\2\2VW\3\2\2\2WY\5\30\r\2XS\3\2\2\2YZ\3\2\2\2ZX\3")
        buf.write("\2\2\2Z[\3\2\2\2[]\3\2\2\2\\^\7\17\2\2]\\\3\2\2\2]^\3")
        buf.write("\2\2\2^\t\3\2\2\2_f\7\b\2\2`b\7\17\2\2a`\3\2\2\2bc\3\2")
        buf.write("\2\2ca\3\2\2\2cd\3\2\2\2de\3\2\2\2eg\5 \21\2fa\3\2\2\2")
        buf.write("gh\3\2\2\2hf\3\2\2\2hi\3\2\2\2ik\3\2\2\2jl\7\17\2\2kj")
        buf.write("\3\2\2\2kl\3\2\2\2l\13\3\2\2\2mn\7\26\2\2n\r\3\2\2\2o")
        buf.write("p\7\26\2\2p\17\3\2\2\2q|\7\t\2\2rt\7\17\2\2sr\3\2\2\2")
        buf.write("tu\3\2\2\2us\3\2\2\2uv\3\2\2\2vx\3\2\2\2wy\5\f\7\2xw\3")
        buf.write("\2\2\2yz\3\2\2\2zx\3\2\2\2z{\3\2\2\2{}\3\2\2\2|s\3\2\2")
        buf.write("\2}~\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\u0081\3\2\2\2")
        buf.write("\u0080\u0082\7\17\2\2\u0081\u0080\3\2\2\2\u0081\u0082")
        buf.write("\3\2\2\2\u0082\21\3\2\2\2\u0083\u008e\7\n\2\2\u0084\u0086")
        buf.write("\7\17\2\2\u0085\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087")
        buf.write("\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u008a\3\2\2\2")
        buf.write("\u0089\u008b\5\f\7\2\u008a\u0089\3\2\2\2\u008b\u008c\3")
        buf.write("\2\2\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008f")
        buf.write("\3\2\2\2\u008e\u0085\3\2\2\2\u008f\u0090\3\2\2\2\u0090")
        buf.write("\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0093\3\2\2\2")
        buf.write("\u0092\u0094\7\17\2\2\u0093\u0092\3\2\2\2\u0093\u0094")
        buf.write("\3\2\2\2\u0094\23\3\2\2\2\u0095\u0097\7\22\2\2\u0096\u0095")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u00a9\3\2\2\2\u0098")
        buf.write("\u009a\7\17\2\2\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2")
        buf.write("\2\u009b\u009c\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009e")
        buf.write("\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u00a2\5\36\20\2\u009f")
        buf.write("\u00a1\7\17\2\2\u00a0\u009f\3\2\2\2\u00a1\u00a4\3\2\2")
        buf.write("\2\u00a2\u00a3\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3\u00a5")
        buf.write("\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a6\t\3\2\2\u00a6")
        buf.write("\u00a8\3\2\2\2\u00a7\u009b\3\2\2\2\u00a8\u00ab\3\2\2\2")
        buf.write("\u00a9\u00aa\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00ac\3")
        buf.write("\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ad\5\36\20\2\u00ad")
        buf.write("\25\3\2\2\2\u00ae\u00af\5\16\b\2\u00af\u00b0\7\3\2\2\u00b0")
        buf.write("\27\3\2\2\2\u00b1\u00b3\5\26\f\2\u00b2\u00b1\3\2\2\2\u00b2")
        buf.write("\u00b3\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b8\5\24\13")
        buf.write("\2\u00b5\u00b7\7\17\2\2\u00b6\u00b5\3\2\2\2\u00b7\u00ba")
        buf.write("\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9")
        buf.write("\u00bb\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb\u00bf\5*\26\2")
        buf.write("\u00bc\u00be\7\17\2\2\u00bd\u00bc\3\2\2\2\u00be\u00c1")
        buf.write("\3\2\2\2\u00bf\u00c0\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0")
        buf.write("\u00c2\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c2\u00c3\7\20\2")
        buf.write("\2\u00c3\31\3\2\2\2\u00c4\u00c6\5\26\f\2\u00c5\u00c4\3")
        buf.write("\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8")
        buf.write("\5\24\13\2\u00c8\33\3\2\2\2\u00c9\u00cd\7\f\2\2\u00ca")
        buf.write("\u00cc\7\5\2\2\u00cb\u00ca\3\2\2\2\u00cc\u00cf\3\2\2\2")
        buf.write("\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00d0\3")
        buf.write("\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d1\7\2\2\3\u00d1\35")
        buf.write("\3\2\2\2\u00d2\u00dd\7\20\2\2\u00d3\u00d7\7\20\2\2\u00d4")
        buf.write("\u00d6\7\17\2\2\u00d5\u00d4\3\2\2\2\u00d6\u00d9\3\2\2")
        buf.write("\2\u00d7\u00d8\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00da")
        buf.write("\3\2\2\2\u00d9\u00d7\3\2\2\2\u00da\u00dd\5\f\7\2\u00db")
        buf.write("\u00dd\5\f\7\2\u00dc\u00d2\3\2\2\2\u00dc\u00d3\3\2\2\2")
        buf.write("\u00dc\u00db\3\2\2\2\u00dd\37\3\2\2\2\u00de\u00e2\5$\23")
        buf.write("\2\u00df\u00e2\5\"\22\2\u00e0\u00e2\5&\24\2\u00e1\u00de")
        buf.write("\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e0\3\2\2\2\u00e2")
        buf.write("!\3\2\2\2\u00e3\u00e4\5(\25\2\u00e4\u00e5\5*\26\2\u00e5")
        buf.write("\u00e6\5\f\7\2\u00e6\u00ec\3\2\2\2\u00e7\u00e8\5\f\7\2")
        buf.write("\u00e8\u00e9\5*\26\2\u00e9\u00ea\5(\25\2\u00ea\u00ec\3")
        buf.write("\2\2\2\u00eb\u00e3\3\2\2\2\u00eb\u00e7\3\2\2\2\u00ec#")
        buf.write("\3\2\2\2\u00ed\u00f1\5(\25\2\u00ee\u00f0\7\17\2\2\u00ef")
        buf.write("\u00ee\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1\u00f2\3\2\2\2")
        buf.write("\u00f1\u00ef\3\2\2\2\u00f2\u00f4\3\2\2\2\u00f3\u00f1\3")
        buf.write("\2\2\2\u00f4\u00f8\5*\26\2\u00f5\u00f7\7\17\2\2\u00f6")
        buf.write("\u00f5\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8\u00f9\3\2\2\2")
        buf.write("\u00f8\u00f6\3\2\2\2\u00f9\u00fb\3\2\2\2\u00fa\u00f8\3")
        buf.write("\2\2\2\u00fb\u00ff\5\f\7\2\u00fc\u00fe\7\17\2\2\u00fd")
        buf.write("\u00fc\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u0100\3\2\2\2")
        buf.write("\u00ff\u00fd\3\2\2\2\u0100\u0102\3\2\2\2\u0101\u00ff\3")
        buf.write("\2\2\2\u0102\u0106\5*\26\2\u0103\u0105\7\17\2\2\u0104")
        buf.write("\u0103\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0107\3\2\2\2")
        buf.write("\u0106\u0104\3\2\2\2\u0107\u0109\3\2\2\2\u0108\u0106\3")
        buf.write("\2\2\2\u0109\u010a\5(\25\2\u010a%\3\2\2\2\u010b\u010f")
        buf.write("\5\f\7\2\u010c\u010e\7\17\2\2\u010d\u010c\3\2\2\2\u010e")
        buf.write("\u0111\3\2\2\2\u010f\u0110\3\2\2\2\u010f\u010d\3\2\2\2")
        buf.write("\u0110\u0112\3\2\2\2\u0111\u010f\3\2\2\2\u0112\u0113\7")
        buf.write("\4\2\2\u0113\'\3\2\2\2\u0114\u0119\7\20\2\2\u0115\u0119")
        buf.write("\7\r\2\2\u0116\u0117\7\22\2\2\u0117\u0119\7\r\2\2\u0118")
        buf.write("\u0114\3\2\2\2\u0118\u0115\3\2\2\2\u0118\u0116\3\2\2\2")
        buf.write("\u0119)\3\2\2\2\u011a\u011b\t\4\2\2\u011b+\3\2\2\2+\60")
        buf.write("\63\669;DKOUZ]chkuz~\u0081\u0087\u008c\u0090\u0093\u0096")
        buf.write("\u009b\u00a2\u00a9\u00b2\u00b8\u00bf\u00c5\u00cd\u00d7")
        buf.write("\u00dc\u00e1\u00eb\u00f1\u00f8\u00ff\u0106\u010f\u0118")
        return buf.getvalue()


class LPParser(Parser):
    grammarFileName = "LP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "':'", "'free'", "<INVALID>", "<INVALID>",
                    "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                    "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                    "<INVALID>", "<INVALID>", "'+'", "'-'", "<INVALID>",
                    "<INVALID>", "'='"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "LF", "MAXIMIZE",
                     "MINIMIZE", "BOUNDS", "BINARIES", "GENERALS", "ST",
                     "END", "INF", "COMMENT", "NEWLINE", "NUMBER", "PLUS",
                     "MINUS", "LEQ", "GEQ", "EQ", "NAME", "SPACES"]

    RULE_prog = 0
    RULE_direction = 1
    RULE_objective_region = 2
    RULE_constraint_region = 3
    RULE_bound_region = 4
    RULE_var_name = 5
    RULE_cstr_name = 6
    RULE_binaries_region = 7
    RULE_generals_region = 8
    RULE_expr = 9
    RULE_naming = 10
    RULE_cstr = 11
    RULE_obj = 12
    RULE_eof = 13
    RULE_term = 14
    RULE_bound = 15
    RULE_onesided_bound = 16
    RULE_twosided_bound = 17
    RULE_bound_free = 18
    RULE_num_or_inf = 19
    RULE_sense = 20

    ruleNames = ["prog", "direction", "objective_region", "constraint_region",
                 "bound_region", "var_name", "cstr_name", "binaries_region",
                 "generals_region", "expr", "naming", "cstr", "obj", "eof",
                 "term", "bound", "onesided_bound", "twosided_bound",
                 "bound_free", "num_or_inf", "sense"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    LF = 3
    MAXIMIZE = 4
    MINIMIZE = 5
    BOUNDS = 6
    BINARIES = 7
    GENERALS = 8
    ST = 9
    END = 10
    INF = 11
    COMMENT = 12
    NEWLINE = 13
    NUMBER = 14
    PLUS = 15
    MINUS = 16
    LEQ = 17
    GEQ = 18
    EQ = 19
    NAME = 20
    SPACES = 21

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def objective_region(self):
            return self.getTypedRuleContext(LPParser.Objective_regionContext, 0)

        def constraint_region(self):
            return self.getTypedRuleContext(LPParser.Constraint_regionContext, 0)

        def bound_region(self):
            return self.getTypedRuleContext(LPParser.Bound_regionContext, 0)

        def eof(self):
            return self.getTypedRuleContext(LPParser.EofContext, 0)

        def generals_region(self):
            return self.getTypedRuleContext(LPParser.Generals_regionContext, 0)

        def binaries_region(self):
            return self.getTypedRuleContext(LPParser.Binaries_regionContext, 0)

        def getRuleIndex(self):
            return LPParser.RULE_prog

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterProg"):
                listener.enterProg(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitProg"):
                listener.exitProg(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitProg"):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)

    def prog(self):

        localctx = LPParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.objective_region()
            self.state = 43
            self.constraint_region()
            self.state = 44
            self.bound_region()
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 4, self._ctx)
            if la_ == 1:
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == LPParser.GENERALS:
                    self.state = 45
                    self.generals_region()

                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == LPParser.BINARIES:
                    self.state = 48
                    self.binaries_region()

                pass

            elif la_ == 2:
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == LPParser.BINARIES:
                    self.state = 51
                    self.binaries_region()

                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == LPParser.GENERALS:
                    self.state = 54
                    self.generals_region()

                pass

            self.state = 59
            self.eof()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAXIMIZE(self):
            return self.getToken(LPParser.MAXIMIZE, 0)

        def MINIMIZE(self):
            return self.getToken(LPParser.MINIMIZE, 0)

        def getRuleIndex(self):
            return LPParser.RULE_direction

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterDirection"):
                listener.enterDirection(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitDirection"):
                listener.exitDirection(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitDirection"):
                return visitor.visitDirection(self)
            else:
                return visitor.visitChildren(self)

    def direction(self):

        localctx = LPParser.DirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_direction)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not (_la == LPParser.MAXIMIZE or _la == LPParser.MINIMIZE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Objective_regionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def direction(self):
            return self.getTypedRuleContext(LPParser.DirectionContext, 0)

        def obj(self):
            return self.getTypedRuleContext(LPParser.ObjContext, 0)

        def LF(self, i: int = None):
            if i is None:
                return self.getTokens(LPParser.LF)
            else:
                return self.getToken(LPParser.LF, i)

        def NEWLINE(self, i: int = None):
            if i is None:
                return self.getTokens(LPParser.NEWLINE)
            else:
                return self.getToken(LPParser.NEWLINE, i)

        def getRuleIndex(self):
            return LPParser.RULE_objective_region

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterObjective_region"):
                listener.enterObjective_region(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitObjective_region"):
                listener.exitObjective_region(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitObjective_region"):
                return visitor.visitObjective_region(self)
            else:
                return visitor.visitChildren(self)

    def objective_region(self):

        localctx = LPParser.Objective_regionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_objective_region)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == LPParser.LF:
                self.state = 63
                self.match(LPParser.LF)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
            self.direction()
            self.state = 71
            self._errHandler.sync(self)
            _alt = 1
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 70
                    self.match(LPParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 6, self._ctx)

            self.state = 75
            self.obj()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == LPParser.NEWLINE:
                self.state = 76
                self.match(LPParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Constraint_regionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ST(self):
            return self.getToken(LPParser.ST, 0)

        def cstr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(LPParser.CstrContext)
            else:
                return self.getTypedRuleContext(LPParser.CstrContext, i)

        def NEWLINE(self, i: int = None):
            if i is None:
                return self.getTokens(LPParser.NEWLINE)
            else:
                return self.getToken(LPParser.NEWLINE, i)

        def getRuleIndex(self):
            return LPParser.RULE_constraint_region

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterConstraint_region"):
                listener.enterConstraint_region(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitConstraint_region"):
                listener.exitConstraint_region(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitConstraint_region"):
                return visitor.visitConstraint_region(self)
            else:
                return visitor.visitChildren(self)

    def constraint_region(self):

        localctx = LPParser.Constraint_regionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_constraint_region)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(LPParser.ST)
            self.state = 86
            self._errHandler.sync(self)
            _alt = 1
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 81
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 80
                            self.match(LPParser.NEWLINE)

                        else:
                            raise NoViableAltException(self)
                        self.state = 83
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input, 8, self._ctx)

                    self.state = 85
                    self.cstr()

                else:
                    raise NoViableAltException(self)
                self.state = 88
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 9, self._ctx)

            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == LPParser.NEWLINE:
                self.state = 90
                self.match(LPParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Bound_regionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOUNDS(self):
            return self.getToken(LPParser.BOUNDS, 0)

        def bound(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(LPParser.BoundContext)
            else:
                return self.getTypedRuleContext(LPParser.BoundContext, i)

        def NEWLINE(self, i: int = None):
            if i is None:
                return self.getTokens(LPParser.NEWLINE)
            else:
                return self.getToken(LPParser.NEWLINE, i)

        def getRuleIndex(self):
            return LPParser.RULE_bound_region

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBound_region"):
                listener.enterBound_region(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBound_region"):
                listener.exitBound_region(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBound_region"):
                return visitor.visitBound_region(self)
            else:
                return visitor.visitChildren(self)

    def bound_region(self):

        localctx = LPParser.Bound_regionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_bound_region)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(LPParser.BOUNDS)
            self.state = 100
            self._errHandler.sync(self)
            _alt = 1
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 95
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 94
                        self.match(LPParser.NEWLINE)
                        self.state = 97
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la == LPParser.NEWLINE):
                            break

                    self.state = 99
                    self.bound()

                else:
                    raise NoViableAltException(self)
                self.state = 102
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 12, self._ctx)

            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == LPParser.NEWLINE:
                self.state = 104
                self.match(LPParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Var_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(LPParser.NAME, 0)

        def getRuleIndex(self):
            return LPParser.RULE_var_name

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVar_name"):
                listener.enterVar_name(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVar_name"):
                listener.exitVar_name(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitVar_name"):
                return visitor.visitVar_name(self)
            else:
                return visitor.visitChildren(self)

    def var_name(self):

        localctx = LPParser.Var_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(LPParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Cstr_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(LPParser.NAME, 0)

        def getRuleIndex(self):
            return LPParser.RULE_cstr_name

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterCstr_name"):
                listener.enterCstr_name(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitCstr_name"):
                listener.exitCstr_name(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitCstr_name"):
                return visitor.visitCstr_name(self)
            else:
                return visitor.visitChildren(self)

    def cstr_name(self):

        localctx = LPParser.Cstr_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cstr_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(LPParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Binaries_regionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BINARIES(self):
            return self.getToken(LPParser.BINARIES, 0)

        def NEWLINE(self, i: int = None):
            if i is None:
                return self.getTokens(LPParser.NEWLINE)
            else:
                return self.getToken(LPParser.NEWLINE, i)

        def var_name(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(LPParser.Var_nameContext)
            else:
                return self.getTypedRuleContext(LPParser.Var_nameContext, i)

        def getRuleIndex(self):
            return LPParser.RULE_binaries_region

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBinaries_region"):
                listener.enterBinaries_region(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBinaries_region"):
                listener.exitBinaries_region(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBinaries_region"):
                return visitor.visitBinaries_region(self)
            else:
                return visitor.visitChildren(self)

    def binaries_region(self):

        localctx = LPParser.Binaries_regionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_binaries_region)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(LPParser.BINARIES)
            self.state = 122
            self._errHandler.sync(self)
            _alt = 1
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 113
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 112
                        self.match(LPParser.NEWLINE)
                        self.state = 115
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la == LPParser.NEWLINE):
                            break

                    self.state = 118
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 117
                        self.var_name()
                        self.state = 120
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la == LPParser.NAME):
                            break


                else:
                    raise NoViableAltException(self)
                self.state = 124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 16, self._ctx)

            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == LPParser.NEWLINE:
                self.state = 126
                self.match(LPParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Generals_regionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GENERALS(self):
            return self.getToken(LPParser.GENERALS, 0)

        def NEWLINE(self, i: int = None):
            if i is None:
                return self.getTokens(LPParser.NEWLINE)
            else:
                return self.getToken(LPParser.NEWLINE, i)

        def var_name(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(LPParser.Var_nameContext)
            else:
                return self.getTypedRuleContext(LPParser.Var_nameContext, i)

        def getRuleIndex(self):
            return LPParser.RULE_generals_region

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterGenerals_region"):
                listener.enterGenerals_region(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitGenerals_region"):
                listener.exitGenerals_region(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitGenerals_region"):
                return visitor.visitGenerals_region(self)
            else:
                return visitor.visitChildren(self)

    def generals_region(self):

        localctx = LPParser.Generals_regionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_generals_region)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(LPParser.GENERALS)
            self.state = 140
            self._errHandler.sync(self)
            _alt = 1
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 131
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 130
                        self.match(LPParser.NEWLINE)
                        self.state = 133
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la == LPParser.NEWLINE):
                            break

                    self.state = 136
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 135
                        self.var_name()
                        self.state = 138
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la == LPParser.NAME):
                            break


                else:
                    raise NoViableAltException(self)
                self.state = 142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 20, self._ctx)

            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == LPParser.NEWLINE:
                self.state = 144
                self.match(LPParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(LPParser.TermContext)
            else:
                return self.getTypedRuleContext(LPParser.TermContext, i)

        def MINUS(self, i: int = None):
            if i is None:
                return self.getTokens(LPParser.MINUS)
            else:
                return self.getToken(LPParser.MINUS, i)

        def PLUS(self, i: int = None):
            if i is None:
                return self.getTokens(LPParser.PLUS)
            else:
                return self.getToken(LPParser.PLUS, i)

        def NEWLINE(self, i: int = None):
            if i is None:
                return self.getTokens(LPParser.NEWLINE)
            else:
                return self.getToken(LPParser.NEWLINE, i)

        def getRuleIndex(self):
            return LPParser.RULE_expr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterExpr"):
                listener.enterExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitExpr"):
                listener.exitExpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitExpr"):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)

    def expr(self):

        localctx = LPParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == LPParser.MINUS:
                self.state = 147
                self.match(LPParser.MINUS)

            self.state = 167
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 25, self._ctx)
            while _alt != 1 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1 + 1:
                    self.state = 153
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input, 23, self._ctx)
                    while _alt != 1 and _alt != ATN.INVALID_ALT_NUMBER:
                        if _alt == 1 + 1:
                            self.state = 150
                            self.match(LPParser.NEWLINE)
                        self.state = 155
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input, 23, self._ctx)

                    self.state = 156
                    self.term()
                    self.state = 160
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input, 24, self._ctx)
                    while _alt != 1 and _alt != ATN.INVALID_ALT_NUMBER:
                        if _alt == 1 + 1:
                            self.state = 157
                            self.match(LPParser.NEWLINE)
                        self.state = 162
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input, 24, self._ctx)

                    self.state = 163
                    _la = self._input.LA(1)
                    if not (_la == LPParser.PLUS or _la == LPParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                self.state = 169
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 25, self._ctx)

            self.state = 170
            self.term()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NamingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cstr_name(self):
            return self.getTypedRuleContext(LPParser.Cstr_nameContext, 0)

        def getRuleIndex(self):
            return LPParser.RULE_naming

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNaming"):
                listener.enterNaming(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNaming"):
                listener.exitNaming(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNaming"):
                return visitor.visitNaming(self)
            else:
                return visitor.visitChildren(self)

    def naming(self):

        localctx = LPParser.NamingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_naming)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.cstr_name()
            self.state = 173
            self.match(LPParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LPParser.ExprContext, 0)

        def sense(self):
            return self.getTypedRuleContext(LPParser.SenseContext, 0)

        def NUMBER(self):
            return self.getToken(LPParser.NUMBER, 0)

        def naming(self):
            return self.getTypedRuleContext(LPParser.NamingContext, 0)

        def NEWLINE(self, i: int = None):
            if i is None:
                return self.getTokens(LPParser.NEWLINE)
            else:
                return self.getToken(LPParser.NEWLINE, i)

        def getRuleIndex(self):
            return LPParser.RULE_cstr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterCstr"):
                listener.enterCstr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitCstr"):
                listener.exitCstr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitCstr"):
                return visitor.visitCstr(self)
            else:
                return visitor.visitChildren(self)

    def cstr(self):

        localctx = LPParser.CstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_cstr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 26, self._ctx)
            if la_ == 1:
                self.state = 175
                self.naming()

            self.state = 178
            self.expr()
            self.state = 182
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 27, self._ctx)
            while _alt != 1 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1 + 1:
                    self.state = 179
                    self.match(LPParser.NEWLINE)
                self.state = 184
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 27, self._ctx)

            self.state = 185
            self.sense()
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 28, self._ctx)
            while _alt != 1 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1 + 1:
                    self.state = 186
                    self.match(LPParser.NEWLINE)
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 28, self._ctx)

            self.state = 192
            self.match(LPParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ObjContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LPParser.ExprContext, 0)

        def naming(self):
            return self.getTypedRuleContext(LPParser.NamingContext, 0)

        def getRuleIndex(self):
            return LPParser.RULE_obj

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterObj"):
                listener.enterObj(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitObj"):
                listener.exitObj(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitObj"):
                return visitor.visitObj(self)
            else:
                return visitor.visitChildren(self)

    def obj(self):

        localctx = LPParser.ObjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_obj)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 29, self._ctx)
            if la_ == 1:
                self.state = 194
                self.naming()

            self.state = 197
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EofContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END(self):
            return self.getToken(LPParser.END, 0)

        def EOF(self):
            return self.getToken(LPParser.EOF, 0)

        def LF(self, i: int = None):
            if i is None:
                return self.getTokens(LPParser.LF)
            else:
                return self.getToken(LPParser.LF, i)

        def getRuleIndex(self):
            return LPParser.RULE_eof

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEof"):
                listener.enterEof(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEof"):
                listener.exitEof(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitEof"):
                return visitor.visitEof(self)
            else:
                return visitor.visitChildren(self)

    def eof(self):

        localctx = LPParser.EofContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_eof)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(LPParser.END)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == LPParser.LF:
                self.state = 200
                self.match(LPParser.LF)
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 206
            self.match(LPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(LPParser.NUMBER, 0)

        def var_name(self):
            return self.getTypedRuleContext(LPParser.Var_nameContext, 0)

        def NEWLINE(self, i: int = None):
            if i is None:
                return self.getTokens(LPParser.NEWLINE)
            else:
                return self.getToken(LPParser.NEWLINE, i)

        def getRuleIndex(self):
            return LPParser.RULE_term

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTerm"):
                listener.enterTerm(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTerm"):
                listener.exitTerm(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitTerm"):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)

    def term(self):

        localctx = LPParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_term)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 32, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.match(LPParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.match(LPParser.NUMBER)
                self.state = 213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 31, self._ctx)
                while _alt != 1 and _alt != ATN.INVALID_ALT_NUMBER:
                    if _alt == 1 + 1:
                        self.state = 210
                        self.match(LPParser.NEWLINE)
                    self.state = 215
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input, 31, self._ctx)

                self.state = 216
                self.var_name()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 217
                self.var_name()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BoundContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def twosided_bound(self):
            return self.getTypedRuleContext(LPParser.Twosided_boundContext, 0)

        def onesided_bound(self):
            return self.getTypedRuleContext(LPParser.Onesided_boundContext, 0)

        def bound_free(self):
            return self.getTypedRuleContext(LPParser.Bound_freeContext, 0)

        def getRuleIndex(self):
            return LPParser.RULE_bound

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBound"):
                listener.enterBound(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBound"):
                listener.exitBound(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBound"):
                return visitor.visitBound(self)
            else:
                return visitor.visitChildren(self)

    def bound(self):

        localctx = LPParser.BoundContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_bound)
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 33, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.twosided_bound()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.onesided_bound()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 222
                self.bound_free()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Onesided_boundContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num_or_inf(self):
            return self.getTypedRuleContext(LPParser.Num_or_infContext, 0)

        def sense(self):
            return self.getTypedRuleContext(LPParser.SenseContext, 0)

        def var_name(self):
            return self.getTypedRuleContext(LPParser.Var_nameContext, 0)

        def getRuleIndex(self):
            return LPParser.RULE_onesided_bound

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterOnesided_bound"):
                listener.enterOnesided_bound(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitOnesided_bound"):
                listener.exitOnesided_bound(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitOnesided_bound"):
                return visitor.visitOnesided_bound(self)
            else:
                return visitor.visitChildren(self)

    def onesided_bound(self):

        localctx = LPParser.Onesided_boundContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_onesided_bound)
        try:
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LPParser.INF, LPParser.NUMBER, LPParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.num_or_inf()
                self.state = 226
                self.sense()
                self.state = 227
                self.var_name()
                pass
            elif token in [LPParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.var_name()
                self.state = 230
                self.sense()
                self.state = 231
                self.num_or_inf()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Twosided_boundContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num_or_inf(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(LPParser.Num_or_infContext)
            else:
                return self.getTypedRuleContext(LPParser.Num_or_infContext, i)

        def sense(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(LPParser.SenseContext)
            else:
                return self.getTypedRuleContext(LPParser.SenseContext, i)

        def var_name(self):
            return self.getTypedRuleContext(LPParser.Var_nameContext, 0)

        def NEWLINE(self, i: int = None):
            if i is None:
                return self.getTokens(LPParser.NEWLINE)
            else:
                return self.getToken(LPParser.NEWLINE, i)

        def getRuleIndex(self):
            return LPParser.RULE_twosided_bound

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTwosided_bound"):
                listener.enterTwosided_bound(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTwosided_bound"):
                listener.exitTwosided_bound(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitTwosided_bound"):
                return visitor.visitTwosided_bound(self)
            else:
                return visitor.visitChildren(self)

    def twosided_bound(self):

        localctx = LPParser.Twosided_boundContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_twosided_bound)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.num_or_inf()
            self.state = 239
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 35, self._ctx)
            while _alt != 1 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1 + 1:
                    self.state = 236
                    self.match(LPParser.NEWLINE)
                self.state = 241
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 35, self._ctx)

            self.state = 242
            self.sense()
            self.state = 246
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 36, self._ctx)
            while _alt != 1 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1 + 1:
                    self.state = 243
                    self.match(LPParser.NEWLINE)
                self.state = 248
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 36, self._ctx)

            self.state = 249
            self.var_name()
            self.state = 253
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 37, self._ctx)
            while _alt != 1 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1 + 1:
                    self.state = 250
                    self.match(LPParser.NEWLINE)
                self.state = 255
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 37, self._ctx)

            self.state = 256
            self.sense()
            self.state = 260
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 38, self._ctx)
            while _alt != 1 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1 + 1:
                    self.state = 257
                    self.match(LPParser.NEWLINE)
                self.state = 262
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 38, self._ctx)

            self.state = 263
            self.num_or_inf()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Bound_freeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_name(self):
            return self.getTypedRuleContext(LPParser.Var_nameContext, 0)

        def NEWLINE(self, i: int = None):
            if i is None:
                return self.getTokens(LPParser.NEWLINE)
            else:
                return self.getToken(LPParser.NEWLINE, i)

        def getRuleIndex(self):
            return LPParser.RULE_bound_free

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBound_free"):
                listener.enterBound_free(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBound_free"):
                listener.exitBound_free(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBound_free"):
                return visitor.visitBound_free(self)
            else:
                return visitor.visitChildren(self)

    def bound_free(self):

        localctx = LPParser.Bound_freeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_bound_free)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.var_name()
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 39, self._ctx)
            while _alt != 1 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1 + 1:
                    self.state = 266
                    self.match(LPParser.NEWLINE)
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 39, self._ctx)

            self.state = 272
            self.match(LPParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Num_or_infContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(LPParser.NUMBER, 0)

        def INF(self):
            return self.getToken(LPParser.INF, 0)

        def MINUS(self):
            return self.getToken(LPParser.MINUS, 0)

        def getRuleIndex(self):
            return LPParser.RULE_num_or_inf

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNum_or_inf"):
                listener.enterNum_or_inf(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNum_or_inf"):
                listener.exitNum_or_inf(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNum_or_inf"):
                return visitor.visitNum_or_inf(self)
            else:
                return visitor.visitChildren(self)

    def num_or_inf(self):

        localctx = LPParser.Num_or_infContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_num_or_inf)
        try:
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LPParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.match(LPParser.NUMBER)
                pass
            elif token in [LPParser.INF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.match(LPParser.INF)
                pass
            elif token in [LPParser.MINUS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 276
                self.match(LPParser.MINUS)
                self.state = 277
                self.match(LPParser.INF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SenseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEQ(self):
            return self.getToken(LPParser.LEQ, 0)

        def EQ(self):
            return self.getToken(LPParser.EQ, 0)

        def GEQ(self):
            return self.getToken(LPParser.GEQ, 0)

        def getRuleIndex(self):
            return LPParser.RULE_sense

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSense"):
                listener.enterSense(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSense"):
                listener.exitSense(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSense"):
                return visitor.visitSense(self)
            else:
                return visitor.visitChildren(self)

    def sense(self):

        localctx = LPParser.SenseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_sense)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            _la = self._input.LA(1)
            if not ((((_la) & ~0x3f) == 0 and (
                    (1 << _la) & ((1 << LPParser.LEQ) | (1 << LPParser.GEQ) | (1 << LPParser.EQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
