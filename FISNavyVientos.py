from numpy import *
from simpful import *
import matplotlib.pylab as plt

class FISNyV:
    FS = FuzzySystem()

    DNE = FuzzySet(function=Triangular_MF(40, 90, 140), term="este")
    DNO = FuzzySet(function=Triangular_MF(220, 270, 320), term="oeste")
    DNS = FuzzySet(function=Triangular_MF(130, 180, 230), term="sur")
    DNN1 = FuzzySet(function=Triangular_MF(0, 0, 50), term="norte1")
    DNN2 = FuzzySet(function=Triangular_MF(310, 360, 365), term="norte2")
    FS.add_linguistic_variable("direccion_navegacion", LinguisticVariable([DNE, DNO, DNS, DNN1, DNN2],
                                                                          concept="Direccion de Navegacion",
                                                                          universe_of_discourse=[0, 360]))

    DVE = FuzzySet(function=Triangular_MF(40, 90, 140), term="este")
    DVO = FuzzySet(function=Triangular_MF(220, 270, 320), term="oeste")
    DVS = FuzzySet(function=Triangular_MF(130, 180, 230), term="sur")
    DVN1 = FuzzySet(function=Triangular_MF(0, 0, 50), term="norte1")
    DVN2 = FuzzySet(function=Triangular_MF(310, 360, 365), term="norte2")
    FS.add_linguistic_variable("direccion_viento", LinguisticVariable([DVE, DVO, DVS, DVN1, DVN2],
                                                                      concept="Direccion del viento",
                                                                      universe_of_discourse=[0, 360]))

    NyV1 = FuzzySet(function=Triangular_MF(0, 0, 4), term="mala")
    NyV2 = FuzzySet(function=Triangular_MF(3, 5, 7), term="media")
    NyV3 = FuzzySet(function=Triangular_MF(6, 8, 9), term="buena")
    NyV4 = FuzzySet(function=Triangular_MF(9, 10, 10), term="excelente")
    FS.add_linguistic_variable("navegacion_viento", LinguisticVariable([NyV1, NyV2, NyV3, NyV4],
                                                                       concept="NavegaciÃ³n y Vientos",
                                                                       universe_of_discourse=[0, 10]))


    FS.add_rules_from_file("ReglasNyV.txt")


    def get_nav_y_vientos(self, nav, viento):
        self.FS.set_variable("direccion_navegacion", nav)
        self.FS.set_variable("direccion_viento", viento)
        return self.FS.Mamdani_inference().get("navegacion_viento")

    def plot_surface(self):
        # Plotting surface
        xs = []
        ys = []
        zs = []
        DIVs = 20
        for x in linspace(0, 360, DIVs):
            for y in linspace(0, 360, DIVs):
                NyV = self.get_nav_y_vientos(x, y)
                xs.append(x)
                ys.append(y)
                zs.append(NyV)
        xs = array(xs)
        ys = array(ys)
        zs = array(zs)

        from mpl_toolkits.mplot3d import Axes3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        xx, yy = plt.meshgrid(xs, ys)

        ax.plot_trisurf(xs, ys, zs, vmin=0, vmax=10, cmap='gnuplot2')
        ax.set_xlabel("Dirección Navegación")
        ax.set_ylabel("Dirección Viento")
        ax.set_zlabel("Calificación")
        ax.set_title("Calificación Navegación y Vientos", pad=20)
        ax.set_zlim(0, 10)
        plt.tight_layout()
        plt.show()


test = FISNyV()
print(test.get_nav_y_vientos(200, 280))
test.plot_surface()