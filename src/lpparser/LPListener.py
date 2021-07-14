from antlr4 import *

if __name__ is not None and "." in __name__:
    from .LPParser import LPParser
else:
    from LPParser import LPParser


# This class defines a complete listener for a parse tree produced by LPParser.
class LPListener(ParseTreeListener):

    # Enter a parse tree produced by LPParser#prog.
    def enterProg(self, ctx: LPParser.ProgContext):
        pass

    # Exit a parse tree produced by LPParser#prog.
    def exitProg(self, ctx: LPParser.ProgContext):
        pass

    # Enter a parse tree produced by LPParser#direction.
    def enterDirection(self, ctx: LPParser.DirectionContext):
        pass

    # Exit a parse tree produced by LPParser#direction.
    def exitDirection(self, ctx: LPParser.DirectionContext):
        pass

    # Enter a parse tree produced by LPParser#objective_region.
    def enterObjective_region(self, ctx: LPParser.Objective_regionContext):
        pass

    # Exit a parse tree produced by LPParser#objective_region.
    def exitObjective_region(self, ctx: LPParser.Objective_regionContext):
        pass

    # Enter a parse tree produced by LPParser#constraint_region.
    def enterConstraint_region(self, ctx: LPParser.Constraint_regionContext):
        pass

    # Exit a parse tree produced by LPParser#constraint_region.
    def exitConstraint_region(self, ctx: LPParser.Constraint_regionContext):
        pass

    # Enter a parse tree produced by LPParser#bound_region.
    def enterBound_region(self, ctx: LPParser.Bound_regionContext):
        pass

    # Exit a parse tree produced by LPParser#bound_region.
    def exitBound_region(self, ctx: LPParser.Bound_regionContext):
        pass

    # Enter a parse tree produced by LPParser#var_name.
    def enterVar_name(self, ctx: LPParser.Var_nameContext):
        pass

    # Exit a parse tree produced by LPParser#var_name.
    def exitVar_name(self, ctx: LPParser.Var_nameContext):
        pass

    # Enter a parse tree produced by LPParser#cstr_name.
    def enterCstr_name(self, ctx: LPParser.Cstr_nameContext):
        pass

    # Exit a parse tree produced by LPParser#cstr_name.
    def exitCstr_name(self, ctx: LPParser.Cstr_nameContext):
        pass

    # Enter a parse tree produced by LPParser#binaries_region.
    def enterBinaries_region(self, ctx: LPParser.Binaries_regionContext):
        pass

    # Exit a parse tree produced by LPParser#binaries_region.
    def exitBinaries_region(self, ctx: LPParser.Binaries_regionContext):
        pass

    # Enter a parse tree produced by LPParser#generals_region.
    def enterGenerals_region(self, ctx: LPParser.Generals_regionContext):
        pass

    # Exit a parse tree produced by LPParser#generals_region.
    def exitGenerals_region(self, ctx: LPParser.Generals_regionContext):
        pass

    # Enter a parse tree produced by LPParser#expr.
    def enterExpr(self, ctx: LPParser.ExprContext):
        pass

    # Exit a parse tree produced by LPParser#expr.
    def exitExpr(self, ctx: LPParser.ExprContext):
        pass

    # Enter a parse tree produced by LPParser#naming.
    def enterNaming(self, ctx: LPParser.NamingContext):
        pass

    # Exit a parse tree produced by LPParser#naming.
    def exitNaming(self, ctx: LPParser.NamingContext):
        pass

    # Enter a parse tree produced by LPParser#cstr.
    def enterCstr(self, ctx: LPParser.CstrContext):
        pass

    # Exit a parse tree produced by LPParser#cstr.
    def exitCstr(self, ctx: LPParser.CstrContext):
        pass

    # Enter a parse tree produced by LPParser#obj.
    def enterObj(self, ctx: LPParser.ObjContext):
        pass

    # Exit a parse tree produced by LPParser#obj.
    def exitObj(self, ctx: LPParser.ObjContext):
        pass

    # Enter a parse tree produced by LPParser#eof.
    def enterEof(self, ctx: LPParser.EofContext):
        pass

    # Exit a parse tree produced by LPParser#eof.
    def exitEof(self, ctx: LPParser.EofContext):
        pass

    # Enter a parse tree produced by LPParser#term.
    def enterTerm(self, ctx: LPParser.TermContext):
        pass

    # Exit a parse tree produced by LPParser#term.
    def exitTerm(self, ctx: LPParser.TermContext):
        pass

    # Enter a parse tree produced by LPParser#bound.
    def enterBound(self, ctx: LPParser.BoundContext):
        pass

    # Exit a parse tree produced by LPParser#bound.
    def exitBound(self, ctx: LPParser.BoundContext):
        pass

    # Enter a parse tree produced by LPParser#onesided_bound.
    def enterOnesided_bound(self, ctx: LPParser.Onesided_boundContext):
        pass

    # Exit a parse tree produced by LPParser#onesided_bound.
    def exitOnesided_bound(self, ctx: LPParser.Onesided_boundContext):
        pass

    # Enter a parse tree produced by LPParser#twosided_bound.
    def enterTwosided_bound(self, ctx: LPParser.Twosided_boundContext):
        pass

    # Exit a parse tree produced by LPParser#twosided_bound.
    def exitTwosided_bound(self, ctx: LPParser.Twosided_boundContext):
        pass

    # Enter a parse tree produced by LPParser#bound_free.
    def enterBound_free(self, ctx: LPParser.Bound_freeContext):
        pass

    # Exit a parse tree produced by LPParser#bound_free.
    def exitBound_free(self, ctx: LPParser.Bound_freeContext):
        pass

    # Enter a parse tree produced by LPParser#num_or_inf.
    def enterNum_or_inf(self, ctx: LPParser.Num_or_infContext):
        pass

    # Exit a parse tree produced by LPParser#num_or_inf.
    def exitNum_or_inf(self, ctx: LPParser.Num_or_infContext):
        pass

    # Enter a parse tree produced by LPParser#sense.
    def enterSense(self, ctx: LPParser.SenseContext):
        pass

    # Exit a parse tree produced by LPParser#sense.
    def exitSense(self, ctx: LPParser.SenseContext):
        pass


del LPParser
