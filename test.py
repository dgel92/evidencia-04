# Máquina de magnetoterapia

# Pruebas unitarias (TDD):

import unittest
from maquina_magnetoterapia import MaquinaMagnetoterapia


class TestMaquinaMagnetoterapia(unittest.TestCase):

    def test_iniciar_sesion(self):
        maquina = MaquinaMagnetoterapia("MagnetoPro 5000")
        maquina.iniciar_sesion(20, 50)  # 20 minutos, 50 Gauss
        self.assertEqual(len(maquina.sesiones), 1)

    def test_ajustar_intensidad(self):
        maquina = MaquinaMagnetoterapia("MagnetoPro 5000")
        maquina.iniciar_sesion(30, 60)
        maquina.ajustar_intensidad(0, 70)
        self.assertEqual(maquina.sesiones[0]["intensidad"], 70)

    def test_calcular_uso_total(self):
        maquina = MaquinaMagnetoterapia("MagnetoPro 5000")
        maquina.iniciar_sesion(20, 50)
        maquina.iniciar_sesion(30, 60)
        self.assertEqual(maquina.calcular_uso_total(), 50)

    def test_repr(self):
        maquina = MaquinaMagnetoterapia("MagnetoPro 5000")
        self.assertEqual(
            str(maquina),
            "MaquinaMagnetoterapia: MagnetoPro 5000, 0 sesiones completadas",
        )

    def test_add(self):
        maquina1 = MaquinaMagnetoterapia("MagnetoPro 5000")
        maquina1.iniciar_sesion(20, 50)
        maquina2 = MaquinaMagnetoterapia("MagnetoTherapy X")
        maquina2.iniciar_sesion(30, 60)
        maquina_total = maquina1 + maquina2
        self.assertEqual(len(maquina_total), 2)


if __name__ == "__main__":
    unittest.main()
