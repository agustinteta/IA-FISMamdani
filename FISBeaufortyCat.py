from simpful import *

class FISByC:
    FS = FuzzySystem()

    # INPUTS
    B1 = FuzzySet(function=Triangular_MF(0, 0, 1.3), term="calma")
    B2 = FuzzySet(function=Trapezoidal_MF(0.7, 1, 3, 3.3), term="ventolina")
    B3 = FuzzySet(function=Trapezoidal_MF(3, 4, 6, 7), term="flojito")
    B4 = FuzzySet(function=Trapezoidal_MF(6, 7, 10, 11), term="flojo")
    B5 = FuzzySet(function=Trapezoidal_MF(10, 11, 16, 17), term="bonancible")
    B6 = FuzzySet(function=Trapezoidal_MF(16, 17, 21, 22), term="fresquito")
    B7 = FuzzySet(function=Trapezoidal_MF(21, 22, 27, 28), term="fresco")
    B8 = FuzzySet(function=Trapezoidal_MF(27, 28, 33, 34), term="frescachon")
    B9 = FuzzySet(function=Trapezoidal_MF(33, 34, 40, 41), term="temporal")
    B10 = FuzzySet(function=Trapezoidal_MF(40, 41, 47, 48), term="temporal_fuerte")
    B11 = FuzzySet(function=Trapezoidal_MF(47, 48, 55, 56), term="temporal_duro")
    B12 = FuzzySet(function=Trapezoidal_MF(55, 56, 63, 64), term="temporal_muy_duro")
    B13 = FuzzySet(function=Trapezoidal_MF(63, 64, 100, 100), term="temporal_huracanado")
    FS.add_linguistic_variable("escala_beaufort", LinguisticVariable([B1, B2, B3, B4, B5, B6, B7, B8,
                                                                      B9, B10, B11, B12, B13],
                                                                     concept="Escala de Beaufort",
                                                                     universe_of_discourse=[0, 71]))

    CB1 = FuzzySet(function=Triangular_MF(0, 0, 0.5), term="a")
    CB2 = FuzzySet(function=Triangular_MF(0.5, 1, 1.5), term="b")
    CB3 = FuzzySet(function=Triangular_MF(1.5, 2, 2.5), term="c")
    CB4 = FuzzySet(function=Triangular_MF(2.5, 3, 3), term="d")
    FS.add_linguistic_variable("categoria_barco", LinguisticVariable([CB1, CB2, CB3, CB4],
                                                                     concept="Categoria del barco",
                                                                     universe_of_discourse=[0, 3]))


    # OUTPUTS
    CE1 = FuzzySet(function=Triangular_MF(0, 0, 2.5), term="mala")
    CE2 = FuzzySet(function=Triangular_MF(2, 5, 8), term="media")
    CE3 = FuzzySet(function=Triangular_MF(6, 10, 10), term="buena")
    FS.add_linguistic_variable("categoria_escala", LinguisticVariable([CE1, CE2, CE3],
                                                                      concept="Categoria del barco y Escala de Beaufort",
                                                                      universe_of_discourse=[0, 10]))

    # REGLAS
    FS.add_rules_from_file("ReglasByC.txt")


    def cat_to_int(self, c):
        categorias = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3
        }
        if c in categorias:
            return categorias[c]
        else:
            return None


    def get_beaufort_categoria(self, beaufort, categoria):

        self.FS.set_variable("escala_beaufort", beaufort)
        self.FS.set_variable("categoria_barco", self.cat_to_int(categoria))
        return self.FS.Mamdani_inference().get("categoria_escala")


test = FISByC()
print(test.get_beaufort_categoria(33, "C"))