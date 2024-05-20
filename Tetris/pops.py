import keyboard
import copy


class Pieza:
    def __init__(self, coordenadas, simbolo="🔳") -> None:
        self.coordenadas = coordenadas  # [x,y]
        self.simbolo = simbolo
        self.pos = 0

    def incrementar(self, item, operacion="+"):
        if operacion == "+":
            elemento_bajo = max(map(lambda x: x[item], self.coordenadas))
        else:
            elemento_bajo = min(map(lambda x: x[item], self.coordenadas))
        if 0 < elemento_bajo and elemento_bajo < 9:
            for i in self.coordenadas:
                if operacion == "+":
                    i[item] += 1
                else:
                    i[item] -= 1

    def caida(self):
        self.incrementar(1)

    def rotar(self):
        # [[0, 0], [0, 1], [1, 1], [2, 1]] iniciales
        # Posicion 0
        # [o][ ][ ]
        # [o][o][o]
        # [ ][ ][ ]
        if self.pos == 0:
            self.coordenadas[0][0] += 2
            self.coordenadas[0][1] += 0
            self.coordenadas[1][0] += 1
            self.coordenadas[1][1] -= 1
            self.coordenadas[2][0] -= 0
            self.coordenadas[2][1] -= 0
            self.coordenadas[3][0] -= 1
            self.coordenadas[3][1] += 1
            # Actualizar posicion despues de actualizar coordenadas
            self.pos += 1
        # Posicion 1
        # [ ][o][o]
        # [ ][o][ ]
        # [ ][o][ ]
        elif self.pos == 1:
            self.coordenadas[0][0] += 0
            self.coordenadas[0][1] += 2
            self.coordenadas[1][0] += 1
            self.coordenadas[1][1] += 1
            self.coordenadas[2][0] -= 0
            self.coordenadas[2][1] -= 0
            self.coordenadas[3][0] -= 1
            self.coordenadas[3][1] -= 1
            # Actualizar posicion despues de actualizar coordenadas
            self.pos += 1
        # Posicion 2
        # [ ][ ][ ]
        # [o][o][o]
        # [ ][ ][o]
        elif self.pos == 2:
            self.coordenadas[0][0] -= 2
            self.coordenadas[0][1] += 0
            self.coordenadas[1][0] -= 1
            self.coordenadas[1][1] += 1
            self.coordenadas[2][0] -= 0
            self.coordenadas[2][1] -= 0
            self.coordenadas[3][0] += 1
            self.coordenadas[3][1] -= 1
            # Actualizar posicion despues de actualizar coordenadas
            self.pos += 1
        # Posicion 3
        # [ ][o][ ]
        # [ ][o][ ]
        # [o][o][ ]
        elif self.pos == 3:
            self.coordenadas[0][0] += 0
            self.coordenadas[0][1] -= 2
            self.coordenadas[1][0] -= 1
            self.coordenadas[1][1] -= 1
            self.coordenadas[2][0] -= 0
            self.coordenadas[2][1] -= 0
            self.coordenadas[3][0] += 1
            self.coordenadas[3][1] += 1
            # Actualizar posicion despues de actualizar coordenadas
            self.pos = 0

    def movimientos(self, movimiento):
        match movimiento:
            case "left":
                self.incrementar(0, operacion="-")
            case "right":
                self.incrementar(0)
            case "down":
                self.caida()
            case "space":
                self.rotar()


class Tablero:
    def __init__(self, ancho, largo):
        self.ancho = ancho
        self.largo = largo
        self.tab_inicial = [
            ["🔲" for _ in range(self.ancho)] for _ in range(self.largo)
        ]

    def imprimir_tablero(self, pieza: Pieza):
        tablero_temporal = copy.deepcopy(self.tab_inicial)
        for coordenada in pieza.coordenadas:
            tablero_temporal[coordenada[1]][coordenada[0]] = pieza.simbolo
        print("\n".join(["".join(i) for i in tablero_temporal]), flush=True)


if __name__ == "__main__":
    l = Pieza(coordenadas=[[0, 0], [0, 1], [1, 1], [2, 1]])
    my_tab = Tablero(10, 10)
    my_tab.imprimir_tablero(pieza=l)
    while True:
        print("Tetris")
        event = keyboard.read_event()
        print("")
        if event.event_type == keyboard.KEY_DOWN:
            l.movimientos(event.name)
            l.caida()
            my_tab.imprimir_tablero(pieza=l)
            if event.name == "esc":
                break
