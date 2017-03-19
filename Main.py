class Main:
    def contarElementos(self,cadena):
        if cadena == [""]:
            return ["0", "0", "0", "0"]
        else:
            return [str(len(cadena)),
                    str(min([int(n) for n in cadena])),
                    str(max([int(n) for n in cadena])),
                    "1.0"
                    ]


