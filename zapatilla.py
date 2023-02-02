class Zapatilla:
    def __init__(self, estilo, talla, color):
        self.talla = talla
        self.color = color
        self.estilo = estilo

    #def __init__(self):
        #self.__talla = 0
        #self.__color = ""
        #self.__estilo = ""

    def get_talla(self):
        return self.__talla

    def get_color(self):
        return self.__color

    def get_estilo(self):
        return self.__estilo

    def set_talla(self, talla):
        self.__talla = talla

    def set_color(self, color):
        self.__color = color

    def set_estilo(self, estilo):
        self.__estilo = estilo