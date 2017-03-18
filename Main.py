class Main:
    def contarElementos(self,cadena):
        if cadena == [""]:
            return ["0", "0"]
        else:
            return [str(len(cadena)), str(min([int(n) for n in cadena]))]

