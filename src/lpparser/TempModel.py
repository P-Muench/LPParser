from collections import defaultdict
from enum import Enum
from typing import DefaultDict, Dict, Set


class VarType(Enum):
    CONTINUOUS = "CONTINUOUS"
    BINARY = "BINARY"
    INTEGER = "INTEGER"
    SEMICONTINUOUS = "SEMICONTINUOUS"


class SENSE(Enum):
    LEQ = "<="
    GEQ = ">="
    EQ = "="


class Direction(Enum):
    MAX = "max"
    MIN = "min"


class TempVar:

    def __init__(self, name, var_type=VarType.CONTINUOUS, lb=0, ub=float("inf")):
        self._name = name
        self._var_type = var_type
        self.lb = lb
        self.ub = ub

    def __repr__(self):
        return f"TempVar({self.name}, {self._var_type}, {self.lb}, {self.ub})"

    def __str__(self):
        return self.name

    def update_bound(self, val, sense: SENSE):
        if sense == SENSE.GEQ:
            self.lb = val
        elif sense == SENSE.LEQ:
            self.ub = val
        elif sense == SENSE.EQ:
            self.ub = val
            self.lb = val
        else:
            raise ValueError(f"Illegal sense {sense}")

    @property
    def name(self):
        return self._name

    @property
    def var_type(self):
        return self._var_type

    @var_type.setter
    def var_type(self, value):
        if value not in VarType:
            raise ValueError("Not a valid Vartype")
        else:
            self._var_type = value

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return TempLinExpr({self: other})
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __add__(self, other):
        if isinstance(other, TempVar):
            coeffed_vars = defaultdict(float)
            coeffed_vars[self] += 1
            coeffed_vars[other] += 1
            return TempLinExpr(coeffed_vars)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-1) * other

    def __rsub__(self, other):
        return (-1) * self + other


class TempLinExpr:

    def __init__(self, coeffed_vars=None):
        if coeffed_vars is None:
            coeffed_vars = defaultdict(float)
        else:
            coeffed_vars = defaultdict(float, coeffed_vars)
        self._coeffed_vars: DefaultDict[TempVar, float] = coeffed_vars

    def iter_coeff_vars(self):
        for var, coeff in self._coeffed_vars.items():
            yield coeff, var

    def __add__(self, other):
        new_coeffed_vars = self._coeffed_vars.copy()
        if isinstance(other, TempLinExpr):
            for var, coeff in other._coeffed_vars.items():
                new_coeffed_vars[var] += coeff
            return TempLinExpr(new_coeffed_vars)
        elif isinstance(other, TempVar):
            new_coeffed_vars[other] += 1
            return TempLinExpr(new_coeffed_vars)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-1) * other

    def __rsub__(self, other):
        return (-1) * self + other

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_coeffed_vars = {var: other * coeff
                                for var, coeff in self._coeffed_vars.items()}
            return TempLinExpr(new_coeffed_vars)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __repr__(self):
        return f"TempLinExpr({repr(self._coeffed_vars)})"

    def __str__(self):
        ret_str = ""
        for var, coeff in self._coeffed_vars.items():
            if coeff == 0:
                continue
            op = "+" if coeff > 0 else "-"
            ret_str += " " + " ".join(s for s in (op, str(abs(coeff)), str(var)))
        return ret_str

    def __le__(self, other):
        if isinstance(other, (int, float)):
            return TempCstr(self, SENSE.LEQ, other)
        return None

    def __ge__(self, other):
        if isinstance(other, (int, float)):
            return TempCstr(self, SENSE.GEQ, other)
        return None

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return TempCstr(self, SENSE.EQ, other)
        return None


class TempCstr:

    def __init__(self, linexpr: TempLinExpr, sense: SENSE, rhs: float):
        if isinstance(linexpr, TempVar):
            linexpr = 1.0 * linexpr
        self._linexpr = linexpr
        self._sense = sense
        self._rhs = rhs

    @property
    def rhs(self):
        return self._rhs

    @property
    def lhs(self):
        return self._linexpr

    @property
    def sense(self):
        return self._sense

    def __repr__(self):
        return f"TempCstr({self._linexpr}, {self._sense}, {self._rhs}"

    def __str__(self):
        return f"{str(self._linexpr)} {self._sense.value} {self._rhs}"


class TempModel:

    def __init__(self, name):
        self.name: str = name
        self._vars: Dict[str, TempVar] = dict()
        self._cstrs: Set[TempCstr] = set()
        self._obj: TempLinExpr = TempLinExpr()
        self.direction = Direction.MIN

    @property
    def vars(self):
        return set(self._vars.values())

    @property
    def cstrs(self):
        return self._cstrs.copy()

    @property
    def obj(self):
        return self._obj

    def add_var(self, var: TempVar):
        if var.name not in self._vars:
            self._vars[var.name] = var

    def set_obj(self, linexpr: TempLinExpr):
        self._obj = linexpr

    def set_dir(self, direction: Direction):
        self.direction = direction

    def add_cstr(self, cstr: TempCstr):
        self._cstrs.add(cstr)

    def get_var_by_name(self, name):
        return self._vars[name]

    def __str__(self):
        return f"{self.name}\n{self.direction.value} {self._obj}\ns.t.\n\t" + \
               "\n\t".join(str(cstr) for cstr in self._cstrs) + \
               "\nVars:\n\t" + "\n\t".join(" <= ".join(str(s) for s in (var.lb, var, var.ub)) + "\t" + var.var_type.value for var in self._vars.values())
