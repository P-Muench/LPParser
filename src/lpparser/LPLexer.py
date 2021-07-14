from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\27")
        buf.write("\u0164\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\5\31\u008e\n\31\3\31\3\31\6\31\u0092\n\31\r\31\16")
        buf.write("\31\u0093\3\32\5\32\u0097\n\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u00a6\n")
        buf.write("\32\3\33\5\33\u00a9\n\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u00b8\n\33\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u00d7\n\35\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\5\36\u00ef\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0100\n\37")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\5!\u0114\n!\3\"\3\"\7\"\u0118\n\"\f\"\16\"\u011b\13")
        buf.write("\"\3\"\3\"\3#\3#\5#\u0121\n#\6#\u0123\n#\r#\16#\u0124")
        buf.write("\3#\6#\u0128\n#\r#\16#\u0129\3$\5$\u012d\n$\3$\6$\u0130")
        buf.write("\n$\r$\16$\u0131\3$\3$\6$\u0136\n$\r$\16$\u0137\5$\u013a")
        buf.write("\n$\3%\3%\3&\3&\3\'\3\'\3\'\3\'\3\'\5\'\u0145\n\'\3(\3")
        buf.write("(\3(\3(\3(\5(\u014c\n(\3)\3)\3*\5*\u0151\n*\3+\3+\5+\u0155")
        buf.write("\n+\3,\3,\7,\u0159\n,\f,\16,\u015c\13,\3-\6-\u015f\n-")
        buf.write("\r-\16-\u0160\3-\3-\2\2.\3\3\5\4\7\2\t\2\13\2\r\2\17\2")
        buf.write("\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\2")
        buf.write(")\2+\2-\2/\2\61\5\63\6\65\7\67\b9\t;\n=\13?\fA\rC\16E")
        buf.write("\17G\20I\21K\22M\23O\24Q\25S\2U\2W\26Y\27\3\2\34\3\2\62")
        buf.write(";\4\2OOoo\4\2CCcc\4\2ZZzz\4\2KKkk\4\2\\\\||\4\2GGgg\4")
        buf.write("\2PPpp\4\2UUuu\4\2WWww\4\2DDdd\4\2LLll\4\2EEee\4\2VVv")
        buf.write("v\4\2QQqq\4\2FFff\4\2[[{{\4\2HHhh\4\2TTtt\4\2IIii\4\2")
        buf.write("NNnn\4\2\f\f\16\17\3\2\60\60\b\2#+..==A\\a}\177\u0080")
        buf.write("\4\2\60\60\62;\4\2\13\13\"\"\2\u0168\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2W\3\2\2\2\2")
        buf.write("Y\3\2\2\2\3[\3\2\2\2\5]\3\2\2\2\7b\3\2\2\2\td\3\2\2\2")
        buf.write("\13f\3\2\2\2\rh\3\2\2\2\17j\3\2\2\2\21l\3\2\2\2\23n\3")
        buf.write("\2\2\2\25p\3\2\2\2\27r\3\2\2\2\31t\3\2\2\2\33v\3\2\2\2")
        buf.write("\35x\3\2\2\2\37z\3\2\2\2!|\3\2\2\2#~\3\2\2\2%\u0080\3")
        buf.write("\2\2\2\'\u0082\3\2\2\2)\u0084\3\2\2\2+\u0086\3\2\2\2-")
        buf.write("\u0088\3\2\2\2/\u008a\3\2\2\2\61\u0091\3\2\2\2\63\u0096")
        buf.write("\3\2\2\2\65\u00a8\3\2\2\2\67\u00b9\3\2\2\29\u00c1\3\2")
        buf.write("\2\2;\u00d8\3\2\2\2=\u00f0\3\2\2\2?\u0101\3\2\2\2A\u0113")
        buf.write("\3\2\2\2C\u0115\3\2\2\2E\u0122\3\2\2\2G\u012c\3\2\2\2")
        buf.write("I\u013b\3\2\2\2K\u013d\3\2\2\2M\u0144\3\2\2\2O\u014b\3")
        buf.write("\2\2\2Q\u014d\3\2\2\2S\u0150\3\2\2\2U\u0154\3\2\2\2W\u0156")
        buf.write("\3\2\2\2Y\u015e\3\2\2\2[\\\7<\2\2\\\4\3\2\2\2]^\7h\2\2")
        buf.write("^_\7t\2\2_`\7g\2\2`a\7g\2\2a\6\3\2\2\2bc\t\2\2\2c\b\3")
        buf.write("\2\2\2de\t\3\2\2e\n\3\2\2\2fg\t\4\2\2g\f\3\2\2\2hi\t\5")
        buf.write("\2\2i\16\3\2\2\2jk\t\6\2\2k\20\3\2\2\2lm\t\7\2\2m\22\3")
        buf.write("\2\2\2no\t\b\2\2o\24\3\2\2\2pq\t\t\2\2q\26\3\2\2\2rs\t")
        buf.write("\n\2\2s\30\3\2\2\2tu\t\13\2\2u\32\3\2\2\2vw\t\f\2\2w\34")
        buf.write("\3\2\2\2xy\t\r\2\2y\36\3\2\2\2z{\t\16\2\2{ \3\2\2\2|}")
        buf.write("\t\17\2\2}\"\3\2\2\2~\177\t\20\2\2\177$\3\2\2\2\u0080")
        buf.write("\u0081\t\21\2\2\u0081&\3\2\2\2\u0082\u0083\t\22\2\2\u0083")
        buf.write("(\3\2\2\2\u0084\u0085\t\23\2\2\u0085*\3\2\2\2\u0086\u0087")
        buf.write("\t\24\2\2\u0087,\3\2\2\2\u0088\u0089\t\25\2\2\u0089.\3")
        buf.write("\2\2\2\u008a\u008b\t\26\2\2\u008b\60\3\2\2\2\u008c\u008e")
        buf.write("\7\17\2\2\u008d\u008c\3\2\2\2\u008d\u008e\3\2\2\2\u008e")
        buf.write("\u008f\3\2\2\2\u008f\u0092\7\f\2\2\u0090\u0092\4\16\17")
        buf.write("\2\u0091\u008d\3\2\2\2\u0091\u0090\3\2\2\2\u0092\u0093")
        buf.write("\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write("\62\3\2\2\2\u0095\u0097\5\61\31\2\u0096\u0095\3\2\2\2")
        buf.write("\u0096\u0097\3\2\2\2\u0097\u00a5\3\2\2\2\u0098\u0099\5")
        buf.write("\t\5\2\u0099\u009a\5\13\6\2\u009a\u009b\5\r\7\2\u009b")
        buf.write("\u009c\5\17\b\2\u009c\u009d\5\t\5\2\u009d\u009e\5\17\b")
        buf.write("\2\u009e\u009f\5\21\t\2\u009f\u00a0\5\23\n\2\u00a0\u00a6")
        buf.write("\3\2\2\2\u00a1\u00a2\5\t\5\2\u00a2\u00a3\5\13\6\2\u00a3")
        buf.write("\u00a4\5\r\7\2\u00a4\u00a6\3\2\2\2\u00a5\u0098\3\2\2\2")
        buf.write("\u00a5\u00a1\3\2\2\2\u00a6\64\3\2\2\2\u00a7\u00a9\5\61")
        buf.write("\31\2\u00a8\u00a7\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00b7")
        buf.write("\3\2\2\2\u00aa\u00ab\5\t\5\2\u00ab\u00ac\5\17\b\2\u00ac")
        buf.write("\u00ad\5\25\13\2\u00ad\u00ae\5\17\b\2\u00ae\u00af\5\t")
        buf.write("\5\2\u00af\u00b0\5\17\b\2\u00b0\u00b1\5\21\t\2\u00b1\u00b2")
        buf.write("\5\23\n\2\u00b2\u00b8\3\2\2\2\u00b3\u00b4\5\t\5\2\u00b4")
        buf.write("\u00b5\5\17\b\2\u00b5\u00b6\5\25\13\2\u00b6\u00b8\3\2")
        buf.write("\2\2\u00b7\u00aa\3\2\2\2\u00b7\u00b3\3\2\2\2\u00b8\66")
        buf.write("\3\2\2\2\u00b9\u00ba\5\61\31\2\u00ba\u00bb\5\33\16\2\u00bb")
        buf.write("\u00bc\5#\22\2\u00bc\u00bd\5\31\r\2\u00bd\u00be\5\25\13")
        buf.write("\2\u00be\u00bf\5%\23\2\u00bf\u00c0\5\27\f\2\u00c08\3\2")
        buf.write("\2\2\u00c1\u00d6\5\61\31\2\u00c2\u00c3\5\33\16\2\u00c3")
        buf.write("\u00c4\5\17\b\2\u00c4\u00c5\5\25\13\2\u00c5\u00d7\3\2")
        buf.write("\2\2\u00c6\u00c7\5\33\16\2\u00c7\u00c8\5\17\b\2\u00c8")
        buf.write("\u00c9\5\25\13\2\u00c9\u00ca\5\13\6\2\u00ca\u00cb\5+\26")
        buf.write("\2\u00cb\u00cc\5\'\24\2\u00cc\u00d7\3\2\2\2\u00cd\u00ce")
        buf.write("\5\33\16\2\u00ce\u00cf\5\17\b\2\u00cf\u00d0\5\25\13\2")
        buf.write("\u00d0\u00d1\5\13\6\2\u00d1\u00d2\5+\26\2\u00d2\u00d3")
        buf.write("\5\17\b\2\u00d3\u00d4\5\23\n\2\u00d4\u00d5\5\27\f\2\u00d5")
        buf.write("\u00d7\3\2\2\2\u00d6\u00c2\3\2\2\2\u00d6\u00c6\3\2\2\2")
        buf.write("\u00d6\u00cd\3\2\2\2\u00d7:\3\2\2\2\u00d8\u00ee\5\61\31")
        buf.write("\2\u00d9\u00da\5-\27\2\u00da\u00db\5\23\n\2\u00db\u00dc")
        buf.write("\5\25\13\2\u00dc\u00dd\5\23\n\2\u00dd\u00de\5+\26\2\u00de")
        buf.write("\u00df\5\13\6\2\u00df\u00e0\5/\30\2\u00e0\u00e1\5\27\f")
        buf.write("\2\u00e1\u00ef\3\2\2\2\u00e2\u00e3\5-\27\2\u00e3\u00e4")
        buf.write("\5\23\n\2\u00e4\u00e5\5\25\13\2\u00e5\u00e6\5\23\n\2\u00e6")
        buf.write("\u00e7\5+\26\2\u00e7\u00e8\5\13\6\2\u00e8\u00e9\5/\30")
        buf.write("\2\u00e9\u00ef\3\2\2\2\u00ea\u00eb\5-\27\2\u00eb\u00ec")
        buf.write("\5\23\n\2\u00ec\u00ed\5\25\13\2\u00ed\u00ef\3\2\2\2\u00ee")
        buf.write("\u00d9\3\2\2\2\u00ee\u00e2\3\2\2\2\u00ee\u00ea\3\2\2\2")
        buf.write("\u00ef<\3\2\2\2\u00f0\u00ff\5\61\31\2\u00f1\u00f2\5\27")
        buf.write("\f\2\u00f2\u00f3\5\31\r\2\u00f3\u00f4\5\33\16\2\u00f4")
        buf.write("\u00f5\5\35\17\2\u00f5\u00f6\5\23\n\2\u00f6\u00f7\5\37")
        buf.write("\20\2\u00f7\u00f8\5!\21\2\u00f8\u00f9\7\"\2\2\u00f9\u00fa")
        buf.write("\5!\21\2\u00fa\u00fb\5#\22\2\u00fb\u0100\3\2\2\2\u00fc")
        buf.write("\u00fd\5\27\f\2\u00fd\u00fe\5!\21\2\u00fe\u0100\3\2\2")
        buf.write("\2\u00ff\u00f1\3\2\2\2\u00ff\u00fc\3\2\2\2\u0100>\3\2")
        buf.write("\2\2\u0101\u0102\5\61\31\2\u0102\u0103\5\23\n\2\u0103")
        buf.write("\u0104\5\25\13\2\u0104\u0105\5%\23\2\u0105@\3\2\2\2\u0106")
        buf.write("\u0107\5\17\b\2\u0107\u0108\5\25\13\2\u0108\u0109\5)\25")
        buf.write("\2\u0109\u010a\5\17\b\2\u010a\u010b\5\25\13\2\u010b\u010c")
        buf.write("\5\17\b\2\u010c\u010d\5!\21\2\u010d\u010e\5\'\24\2\u010e")
        buf.write("\u0114\3\2\2\2\u010f\u0110\5\17\b\2\u0110\u0111\5\25\13")
        buf.write("\2\u0111\u0112\5)\25\2\u0112\u0114\3\2\2\2\u0113\u0106")
        buf.write("\3\2\2\2\u0113\u010f\3\2\2\2\u0114B\3\2\2\2\u0115\u0119")
        buf.write("\7^\2\2\u0116\u0118\n\27\2\2\u0117\u0116\3\2\2\2\u0118")
        buf.write("\u011b\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u011a\3\2\2\2")
        buf.write("\u011a\u011c\3\2\2\2\u011b\u0119\3\2\2\2\u011c\u011d\b")
        buf.write("\"\2\2\u011dD\3\2\2\2\u011e\u0120\5\61\31\2\u011f\u0121")
        buf.write("\5Y-\2\u0120\u011f\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0123")
        buf.write("\3\2\2\2\u0122\u011e\3\2\2\2\u0123\u0124\3\2\2\2\u0124")
        buf.write("\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0127\3\2\2\2")
        buf.write("\u0126\u0128\5Y-\2\u0127\u0126\3\2\2\2\u0128\u0129\3\2")
        buf.write("\2\2\u0129\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012aF\3")
        buf.write("\2\2\2\u012b\u012d\5K&\2\u012c\u012b\3\2\2\2\u012c\u012d")
        buf.write("\3\2\2\2\u012d\u012f\3\2\2\2\u012e\u0130\5\7\4\2\u012f")
        buf.write("\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u012f\3\2\2\2")
        buf.write("\u0131\u0132\3\2\2\2\u0132\u0139\3\2\2\2\u0133\u0135\t")
        buf.write("\30\2\2\u0134\u0136\5\7\4\2\u0135\u0134\3\2\2\2\u0136")
        buf.write("\u0137\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2")
        buf.write("\u0138\u013a\3\2\2\2\u0139\u0133\3\2\2\2\u0139\u013a\3")
        buf.write("\2\2\2\u013aH\3\2\2\2\u013b\u013c\7-\2\2\u013cJ\3\2\2")
        buf.write("\2\u013d\u013e\7/\2\2\u013eL\3\2\2\2\u013f\u0140\7>\2")
        buf.write("\2\u0140\u0145\7?\2\2\u0141\u0145\7>\2\2\u0142\u0143\7")
        buf.write("?\2\2\u0143\u0145\7>\2\2\u0144\u013f\3\2\2\2\u0144\u0141")
        buf.write("\3\2\2\2\u0144\u0142\3\2\2\2\u0145N\3\2\2\2\u0146\u0147")
        buf.write("\7@\2\2\u0147\u014c\7?\2\2\u0148\u014c\7@\2\2\u0149\u014a")
        buf.write("\7?\2\2\u014a\u014c\7@\2\2\u014b\u0146\3\2\2\2\u014b\u0148")
        buf.write("\3\2\2\2\u014b\u0149\3\2\2\2\u014cP\3\2\2\2\u014d\u014e")
        buf.write("\7?\2\2\u014eR\3\2\2\2\u014f\u0151\t\31\2\2\u0150\u014f")
        buf.write("\3\2\2\2\u0151T\3\2\2\2\u0152\u0155\5S*\2\u0153\u0155")
        buf.write("\t\32\2\2\u0154\u0152\3\2\2\2\u0154\u0153\3\2\2\2\u0155")
        buf.write("V\3\2\2\2\u0156\u015a\5S*\2\u0157\u0159\5U+\2\u0158\u0157")
        buf.write("\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158\3\2\2\2\u015a")
        buf.write("\u015b\3\2\2\2\u015bX\3\2\2\2\u015c\u015a\3\2\2\2\u015d")
        buf.write("\u015f\t\33\2\2\u015e\u015d\3\2\2\2\u015f\u0160\3\2\2")
        buf.write("\2\u0160\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0162")
        buf.write("\3\2\2\2\u0162\u0163\b-\2\2\u0163Z\3\2\2\2\34\2\u008d")
        buf.write("\u0091\u0093\u0096\u00a5\u00a8\u00b7\u00d6\u00ee\u00ff")
        buf.write("\u0113\u0119\u0120\u0124\u0129\u012c\u0131\u0137\u0139")
        buf.write("\u0144\u014b\u0150\u0154\u015a\u0160\3\b\2\2")
        return buf.getvalue()


class LPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

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

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'free'", "'+'", "'-'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "LF", "MAXIMIZE", "MINIMIZE", "BOUNDS", "BINARIES", "GENERALS", 
            "ST", "END", "INF", "COMMENT", "NEWLINE", "NUMBER", "PLUS", 
            "MINUS", "LEQ", "GEQ", "EQ", "NAME", "SPACES" ]

    ruleNames = [ "T__0", "T__1", "DIGIT", "M", "A", "X", "I", "Z", "E", 
                  "N", "S", "U", "B", "J", "C", "T", "O", "D", "Y", "F", 
                  "R", "G", "L", "LF", "MAXIMIZE", "MINIMIZE", "BOUNDS", 
                  "BINARIES", "GENERALS", "ST", "END", "INF", "COMMENT", 
                  "NEWLINE", "NUMBER", "PLUS", "MINUS", "LEQ", "GEQ", "EQ", 
                  "NAMESTART", "NAMECONT", "NAME", "SPACES" ]

    grammarFileName = "LP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


