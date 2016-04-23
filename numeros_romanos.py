"""Baseado no Dojo http://dojopuzzles.com/problemas/exibe/numeros-romanos/"""
from unittest import TestCase


class NumeroRomano(object):
    _numeros_basicos = (
        (1000, "M"),
        (500, "D"),
        (100, "C"),
        (50, "L"),
        (10, "X"),
        (5, "V"),
        (1, "I")
    )

    def __init__(self, numero):
        self._numero = numero

    def __str__(self):
        return self._numero_romano(self._numero)

    def _numero_romano(self, numero):
        total = ""
        for number, word in self._numeros_basicos:
            while numero >= number:
                numero -= number
                total += word

        return total.\
            replace("DCCCC", "CM").\
            replace("CCCC", "CD").\
            replace("LXXXX", "XC").\
            replace("XXXX", "XL").\
            replace("VIIII", "IX").\
            replace("IIII", "IV")


class NumeroRomanoTest(TestCase):
    def test_roman(self):
        import roman

        number = 1

        while number <= 1000:
            with self.subTest():
                self.assertEqual(roman.toRoman(number), str(NumeroRomano(number)))
                number += 1
