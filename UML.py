class cosa:
    def __init__(self, publico:str = "publico",protegido:str = "protegido",privado:str="privado"):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado

    def informacion(self):
        print(
            (
               f"Esta es una clase con atributos publicos: {self.publico}, "
                f"un atributo protegido: {self._protegido}, "
                f"y un atributo privado: {self.__privado}"
            )
        )

e=cosa()
print(e.publico)
print(e._protegido)
print(e.__privado)
