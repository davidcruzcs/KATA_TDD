class Main:
    def contarElementos(self,cadena):
        if cadena == [""]:
            return ["0", "0", "0", "0"]
        else:
            if len(cadena) <= 2:
                return [str(len(cadena)),
                        str(min([int(n) for n in cadena])),
                        str(max([int(n) for n in cadena])),
                        str(sum([int(n) for n in cadena]) / float(len(cadena)))
                        ]
            else:
                return [str(len(cadena)),
                        str(min([int(n) for n in cadena])),
                        str(max([int(n) for n in cadena])),
                        "1.0"
                        ]




