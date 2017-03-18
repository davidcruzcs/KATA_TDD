class Main:
    def contarElementos(self,cadena):
        if cadena == [""]:
            return ["0", "0"]
        elif len(cadena) == 1 :
            return [str(len(cadena)), cadena[0]]
        else:
            return [str(len(cadena))]

