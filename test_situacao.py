
import unittest

from situacao import situacao

CASOS_VALIDOS = [
    (0.0, 80, "REPROVADO"),
    (3.9, 80, "REPROVADO"),
    (4.0, 80, "RECUPERACAO"),
    (6.9, 80, "RECUPERACAO"),
    (7.0, 80, "APROVADO"),
    (10.0, 80, "APROVADO"),
    (8.0, 0, "REPROVADO_POR_FALTA"),
    (8.0, 74, "REPROVADO_POR_FALTA"),
    (8.0, 75, "APROVADO"),
    (8.0, 100, "APROVADO"),
    (2.0, 50, "REPROVADO_POR_FALTA"),
]

class TesteSituacao(unittest.TestCase):

    def test_casos_validos(self):
        for media, frequencia, esperado in CASOS_VALIDOS:
            with self.subTest(media=media, frequencia=frequencia):
                self.assertEqual(
                    situacao(media, frequencia),
                    esperado
                )

    def test_media_abaixo_do_limite(self):
        with self.assertRaises(ValueError):
            situacao(-0.1, 80)

    def test_media_acima_do_limite(self):
        with self.assertRaises(ValueError):
            situacao(10.1, 80)

    def test_frequencia_abaixo_do_limite(self):
        with self.assertRaises(ValueError):
            situacao(8.0, -1)

    def test_frequencia_acima_do_limite(self):
        with self.assertRaises(ValueError):
            situacao(8.0, 101)

if __name__ == "__main__":
    unittest.main(verbosity=2)
