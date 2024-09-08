# Máquina de hacer botones


class MaquinaMagnetoterapia:
    def __init__(self, modelo):
        self.modelo = modelo
        self.sesiones = []

    def iniciar_sesion(self, duracion, intensidad):
        sesion = {
            "duracion": duracion,  # en minutos
            "intensidad": intensidad,  # en Gauss
        }
        self.sesiones.append(sesion)

    def ajustar_intensidad(self, index, nueva_intensidad):
        if index < len(self.sesiones):
            self.sesiones[index]["intensidad"] = nueva_intensidad

    def calcular_uso_total(self):
        return sum(s["duracion"] for s in self.sesiones)

    def __len__(self):
        return len(self.sesiones)

    def __add__(self, other):
        nueva_maquina = MaquinaMagnetoterapia(self.modelo + " + " + other.modelo)
        nueva_maquina.sesiones = self.sesiones + other.sesiones
        return nueva_maquina

    def __str__(self):
        return f"MaquinaMagnetoterapia: {self.modelo}, {len(self.sesiones)} sesiones completadas"
