from ortools.linear_solver import pywraplp
from lpparser import TempModel, VarType, Direction, SENSE


def realize(temp_model: TempModel, solver="SCIP") -> pywraplp.Solver:
    m: pywraplp.Solver = pywraplp.Solver.CreateSolver(solver)
    inf = m.Infinity()

    def parse_bound(bnd):
        if bnd == float("inf"):
            return inf
        elif bnd == float("-inf"):
            return - inf
        else:
            return bnd

    var_mapping = dict()
    for temp_var in temp_model.vars:
        if temp_var.var_type == VarType.BINARY:
            var: pywraplp.Variable = m.BoolVar(temp_var.name)
            var.SetBounds(lb=parse_bound(temp_var.lb), ub=parse_bound(temp_var.ub))
        elif temp_var.var_type == VarType.CONTINUOUS:
            var = m.NumVar(name=temp_var.name, lb=parse_bound(temp_var.lb), ub=parse_bound(temp_var.ub))
        elif temp_var.var_type == VarType.INTEGER:
            var = m.IntVar(name=temp_var.name, lb=parse_bound(temp_var.lb), ub=parse_bound(temp_var.ub))
        else:
            raise ValueError(f"Unsupported Variable type {temp_var.var_type.value}")
        var_mapping[temp_var] = var

    for temp_cstr in temp_model.cstrs:
        if temp_cstr.sense == SENSE.LEQ:
            cstr: pywraplp.Constraint = m.Constraint(-inf, temp_cstr.rhs)
        elif temp_cstr.sense == SENSE.GEQ:
            cstr: pywraplp.Constraint = m.Constraint(temp_cstr.rhs, inf)
        else:
            cstr: pywraplp.Constraint = m.Constraint(temp_cstr.rhs, temp_cstr.rhs)
        for coef, temp_var in temp_cstr.lhs.iter_coeff_vars():
            cstr.SetCoefficient(var_mapping[temp_var], coef)

    objective = m.Objective()
    for coef, temp_var in temp_model.obj.iter_coeff_vars():
        objective.SetCoefficient(var_mapping[temp_var], coef)

    if temp_model.direction == Direction.MAX:
        objective.SetMaximization()
    else:
        objective.SetMinimization()

    return m
