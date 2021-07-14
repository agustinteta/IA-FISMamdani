from simpful import *
from FISBeaufortyCat import FISByC
from FISNavyVientos import FISNyV


FS = FuzzySystem()

# -------------------------------INICIO INPUTS --------------------------------------------
NyV1 = FuzzySet(function=Triangular_MF(0, 0, 4), term="mala")
NyV2 = FuzzySet(function=Triangular_MF(3, 5, 7), term="media")
NyV3 = FuzzySet(function=Triangular_MF(6, 8, 9), term="buena")
NyV4 = FuzzySet(function=Triangular_MF(9, 10, 10), term="excelente")
FS.add_linguistic_variable("navegacion_viento", LinguisticVariable([NyV1, NyV2, NyV3, NyV4],
                                                                   concept="Navegación y Vientos",
                                                                   universe_of_discourse=[0, 10]))

CE1 = FuzzySet(function=Triangular_MF(0, 0, 2.5), term="mala")
CE2 = FuzzySet(function=Triangular_MF(2, 5, 8), term="media")
CE3 = FuzzySet(function=Triangular_MF(6, 10, 10), term="buena")
FS.add_linguistic_variable("categoria_escala", LinguisticVariable([CE1, CE2, CE3],
                                                                  concept="Categoria del barco y Escala de Beaufort",
                                                                  universe_of_discourse=[0, 10]))


N1 = FuzzySet(function=Trapezoidal_MF(0, 0, 1500, 2500), term="bajas")
N2 = FuzzySet(function=Trapezoidal_MF(1500, 2500, 5500, 6500), term="medias")
N3 = FuzzySet(function=Trapezoidal_MF(5500, 6000, 12000, 12000), term="altas")
FS.add_linguistic_variable("altura_nubes", LinguisticVariable([N1, N2, N3],
                                                              concept="Altura de las nubes",
                                                              universe_of_discourse=[0, 11000]))


# -------------------------------FIN INPUTS ------------------------------------------------


# -------------------------------INICIO OUTPUTS --------------------------------------------
CD1 = FuzzySet(function=Triangular_MF(0, 0, 2.5), term="mala")
CD2 = FuzzySet(function=Triangular_MF(2, 4, 6), term="mediocre")
CD3 = FuzzySet(function=Triangular_MF(5, 7, 9), term="buena")
CD4 = FuzzySet(function=Triangular_MF(7.5, 10, 10), term="excelente")
FS.add_linguistic_variable("clasificacion_dia", LinguisticVariable([CD1, CD2, CD3, CD4],
                                                                   concept="Clasificación del día",
                                                                   universe_of_discourse=[0, 10]))

# -------------------------------FIN OUTPUTS ------------------------------------------------
FS.add_rules_from_file("ReglasMain.txt")

FISNyV = FISNyV()
FISByC = FISByC()

FS.set_variable("navegacion_viento", FISNyV.get_nav_y_vientos(0, 0))
FS.set_variable("categoria_escala", FISByC.get_beaufort_categoria(30, "A"))
FS.set_variable("altura_nubes", 10000)

print(FS.inference())

