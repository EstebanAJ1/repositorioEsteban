class ave:
    def _init_(self, tipo, vuela):
        self.ave = tipo 
        self.vuelo = vuela
        self.oviparos = True
        self.pico = True

    def comer(self, comida):
        print("Este tipo de ave come normalmente :", comida)

    def volar(self):
        print("este tipo de ave puede volar:", self.vuelo)
        