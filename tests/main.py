import src.LPReader as LPReader
from src.ModelRealizer import realize


def main(filename):
    tmp_model = LPReader.read(filename)
    model = realize(tmp_model)

    model.Solve()
    # for var in model.variables():
    #     print(var.name, var.solution_value())

    print('Objective value =', model.Objective().Value())
    assert model.Objective().Value() == 924


if __name__ == '__main__':
    main("resources/lp_examples/10teams.lp")
