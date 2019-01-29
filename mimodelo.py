class OrdenamientoSeleccion(object):

    def ordenarSeleccion(self, Arreglo):
        for x in range(0, len(Arreglo)-1):
            maspequenio =x
            for i in range(x+1, len(Arreglo)):
                if Arreglo[i] < Arreglo[maspequenio]:
                    maspequenio = i
            if maspequenio != x:
                temp = Arreglo[x]
                Arreglo[x] = Arreglo[maspequenio]
                Arreglo[maspequenio] = temp
            print(Arreglo)
        print(Arreglo)

    def ordenarInsercion(self, Arreglo):
        for x in range(1, len(Arreglo)):
            aux = Arreglo[x]
            posicion = x
            while posicion > 0 and Arreglo[posicion - 1] > aux:
                Arreglo[posicion] = Arreglo[posicion - 1]
                posicion = posicion -1
                Arreglo[posicion] = aux
            print(Arreglo)


        print(Arreglo)

