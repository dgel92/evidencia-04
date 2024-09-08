class MaquinaMagnetoterapia:
    def __init__(self, modelo):
        self.__modelo = modelo
        self.__sesiones = []

    def __iniciar_sesion(self, duracion, intensidad):
        sesion = {
            "duracion": duracion,  # minutos
            "intensidad": intensidad,  # Gauss
        }
        self.__sesiones.append(sesion)

    def __ajustar_intensidad(self, index, nueva_intensidad):
        if index < len(self.__sesiones):
            self.__sesiones[index]["intensidad"] = nueva_intensidad

    def __calcular_uso_total(self):
        return sum(s["duracion"] for s in self.__sesiones)

    def __len__(self):
        return len(self.__sesiones)

    def __add__(self, other):
        nueva_maquina = MaquinaMagnetoterapia(self.__modelo + " + " + other.__modelo)
        nueva_maquina.__sesiones = self.__sesiones + other.__sesiones
        return nueva_maquina

    def __str__(self):
        return f"MaquinaMagnetoterapia: {self.__modelo}, {len(self.__sesiones)} sesiones completadas"

    # Métodos públicos para pruebas
    def iniciar_sesion(self, duracion, intensidad):
        self.__iniciar_sesion(duracion, intensidad)

    def ajustar_intensidad(self, index, nueva_intensidad):
        self.__ajustar_intensidad(index, nueva_intensidad)

    def calcular_uso_total(self):
        return self.__calcular_uso_total()

    def ver_sesiones(self):
        return self.__sesiones
