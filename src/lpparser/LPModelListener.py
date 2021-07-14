from antlr4 import *
from lpparser.LPParser import LPParser
from lpparser.LPListener import LPListener
from lpparser.TempModel import VarType, TempVar, SENSE, TempLinExpr, TempCstr, Direction, TempModel


class LPModelListener(LPListener):

    def __init__(self):
        self.tmp_model = TempModel("")

    def exitVar_name(self, ctx: LPParser.Var_nameContext):
        var_name = ctx.NAME().getText()
        self.tmp_model.add_var(TempVar(var_name))

    def exitBinaries_region(self, ctx: LPParser.Binaries_regionContext):
        for var in ctx.getTypedRuleContexts(LPParser.Var_nameContext):
            var_name = var.NAME().getText()
            self.tmp_model.get_var_by_name(var_name).var_type = VarType.BINARY

    def exitGenerals_region(self, ctx: LPParser.Generals_regionContext):
        for var in ctx.getTypedRuleContexts(LPParser.Var_nameContext):
            var_name = var.NAME().getText()
            self.tmp_model.get_var_by_name(var_name).var_type = VarType.INTEGER

    def exitObj(self, ctx: LPParser.ObjContext):
        self.tmp_model.set_obj(self.parse_expr(ctx.expr()))

    def exitObjective_region(self, ctx:LPParser.Objective_regionContext):
        dir = ctx.direction()
        if dir.MAXIMIZE():
            self.tmp_model.set_dir(Direction.MAX)

    def exitBound_free(self, ctx:LPParser.Bound_freeContext):
        var = self.tmp_model.get_var_by_name(ctx.var_name().getText())
        var.lb = float("-inf")
        var.ub = float("inf")

    def exitOnesided_bound(self, ctx:LPParser.Onesided_boundContext):
        var = self.tmp_model.get_var_by_name(ctx.var_name().getText())
        sense = self.parse_sense(ctx.sense())
        num = self.parse_num_or_inf(ctx.num_or_inf())
        if ctx.var_name().start.start <= ctx.sense().start.start:
            # var sense num
            var.update_bound(num, sense)
        else:
            # num sense var = var esnes num (swap sense)
            sense = self._swap_sense(sense)
            var.update_bound(num, sense)

    def _swap_sense(self, sense):
        if sense == SENSE.EQ:
            return sense
        return SENSE.GEQ if sense == SENSE.LEQ else SENSE.LEQ

    def exitTwosided_bound(self, ctx:LPParser.Twosided_boundContext):
        var = self.tmp_model.get_var_by_name(ctx.var_name().getText())
        sense1 = self.parse_sense(ctx.sense(0))
        sense2 = self.parse_sense(ctx.sense(1))
        num1 = self.parse_num_or_inf(ctx.num_or_inf(0))
        num2 = self.parse_num_or_inf(ctx.num_or_inf(1))
        # num1 sense1 var = var 1esnes num1 (swap sense1)
        sense1 = self._swap_sense(sense1)
        var.update_bound(num1, sense1)
        # var sense2 num2
        var.update_bound(num2, sense2)


    @staticmethod
    def parse_num_or_inf(num_or_inf_ctx: LPParser.Num_or_infContext):
        if num_or_inf_ctx.NUMBER():
            num = float(num_or_inf_ctx.NUMBER().getText())
        elif num_or_inf_ctx.MINUS():
            num = float("-inf")
        elif num_or_inf_ctx.INF():
            num = float("inf")
        else:
            raise ValueError()
        return num

    def exitCstr(self, ctx: LPParser.CstrContext):
        expr = self.parse_expr(ctx.expr())

        sense = self.parse_sense(ctx.sense())
        b = float(ctx.NUMBER().getText())
        self.tmp_model.add_cstr(TempCstr(expr, sense, b))

    @staticmethod
    def parse_sense(sense_ctx):
        if sense_ctx.GEQ():
            sense = SENSE.GEQ
        elif sense_ctx.LEQ():
            sense = SENSE.LEQ
        else:
            sense = SENSE.EQ
        return sense

    def parse_expr(self, ctx: LPParser.ExprContext):
        tmp_cstr = TempLinExpr()
        op = "+"
        for c in ctx.children:
            if isinstance(c, TerminalNode):
                op = c.getText()
            elif isinstance(c, LPParser.TermContext):
                coeff = c.NUMBER()
                if coeff is None:
                    coeff = 1
                else:
                    coeff = coeff.getText()
                coeff = float(coeff)
                var_name = c.var_name().NAME().getText()
                var = self.tmp_model.get_var_by_name(var_name)
                if op == "+":
                    tmp_cstr = tmp_cstr + coeff * var
                elif op == "-":
                    tmp_cstr = tmp_cstr - coeff * var
                else:
                    raise ValueError()
        return tmp_cstr


def test():
    x1, x2, x3 = TempVar("x1"), TempVar("x2"), TempVar("x3")
    print(x1 + 2 * x2 - x3)


if __name__ == '__main__':
    test()
