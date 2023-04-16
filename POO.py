#Humberto Hernández Trejo

class Vehiculo:
    def init(self, tipo="No definido", modelo="No definido", color="No definido"):
        #atributos de la clase
        self._tipo = tipo
        self._modelo = modelo
        self._color = color
    #metodos para generar el estado del vehiculo
    def estado(self):
        print(f"Tipo: {self._tipo}") #f es instancia
        print(f"Modelo: {self._modelo}")
        print(f"Color: {self._color}")

    # getters y setters para los atributos privados
    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo):
        self._tipo = tipo

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

class Coche(Vehiculo):
    def init(self, tipo="No definido", modelo="No definido", color="No definido", puertas=0, velocidad_maxima=0):
        super().init(tipo, modelo, color)
        #atributos de la subclase
        self._puertas = puertas
        self._velocidad_maxima = velocidad_maxima

    def estado(self):
        super().estado()
        #metodos que muestran parte del estado del vehiculo 
        print(f"Puertas: {self._puertas}")
        print(f"Velocidad máxima: {self._velocidad_maxima} km/h")

    # getters y setters para los atributos privados
    def get_puertas(self):
        return self._puertas

    def set_puertas(self, puertas):
        self._puertas = puertas

    def get_velocidad_maxima(self):
        return self._velocidad_maxima

    def set_velocidad_maxima(self, velocidad_maxima):
        self._velocidad_maxima = velocidad_maxima

#abstaccion
coche = Coche()
coche.set_tipo("Coche")
coche.set_modelo("Mustang")
coche.set_color("Rojo")
coche.set_puertas(2)
coche.set_velocidad_maxima(250)

print()
coche.estado()
print()

coche.set_velocidad_maxima(300)

coche.estado()