from antlr4 import *

if __name__ is not None and "." in __name__:
    from .LPParser import LPParser
else:
    from LPParser import LPParser


# This class defines a complete generic visitor for a parse tree produced by LPParser.

class LPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LPParser#prog.
    def visitProg(self, ctx: LPParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LPParser#direction.
    def visitDirection(self, ctx: LPParser.DirectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LPParser#objective_region.
    def visitObjective_region(self, ctx: LPParser.Objective_regionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LPParser#constraint_region.
    def visitConstraint_region(self, ctx: LPParser.Constraint_regionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LPParser#bound_region.
    def visitBound_region(self, ctx: LPParser.Bound_regionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LPParser#var_name.
    def visitVar_name(self, ctx: LPParser.Var_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LPParser#cstr_name.
    def visitCstr_name(self, ctx: LPParser.Cstr_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LPParser#binaries_region.
    def visitBinaries_region(self, ctx: LPParser.Binaries_regionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LPParser#generals_region.
    def visitGenerals_region(self, ctx: LPParser.Generals_regionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LPParser#expr.
    def visitExpr(self, ctx: LPParser.ExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LPParser#naming.
    def visitNaming(self, ctx: LPParser.NamingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LPParser#cstr.
    def visitCstr(self, ctx: LPParser.CstrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LPParser#obj.
    def visitObj(self, ctx: LPParser.ObjContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LPParser#eof.
    def visitEof(self, ctx: LPParser.EofContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LPParser#term.
    def visitTerm(self, ctx: LPParser.TermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LPParser#bound.
    def visitBound(self, ctx: LPParser.BoundContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LPParser#onesided_bound.
    def visitOnesided_bound(self, ctx: LPParser.Onesided_boundContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LPParser#twosided_bound.
    def visitTwosided_bound(self, ctx: LPParser.Twosided_boundContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LPParser#bound_free.
    def visitBound_free(self, ctx: LPParser.Bound_freeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LPParser#num_or_inf.
    def visitNum_or_inf(self, ctx: LPParser.Num_or_infContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LPParser#sense.
    def visitSense(self, ctx: LPParser.SenseContext):
        return self.visitChildren(ctx)


del LPParser
