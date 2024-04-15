import unittest 
# def vocal_counter (palabra):
#     vocales = ("a", "e", "i", "o", "u")
#     resultado = {}
#     for letra in palabra: 
#         if letra in vocales:
#             # if not resultado.get(letra):
#             #     resultado[letra] = 0
#             # resultado += 1 
#             if letra in resultado.keys():

#                 resultado [letra] += 1 
#             else:
#                 resultado [letra] = 1 
#     return resultado

def vocal_counter (word:str) -> dict : 
    vocal = {}
    word = word.lower ()
    for letter in word : 
        if letter in ("a","e","i","o","u"):
            vocal [letter] = 1 + vocal.get(letter,0)
    return vocal

# class TestContarVocales(unittest.TestCase):
#     def test_con_todas_las_vocales(self):
#         palabra = "mucrielago"
#         resultado = vocal_counter(palabra)
#         self.assertEqual(resultado, {
#             "a" :1, "e" : 1, "i" : 1 , "o" : 1, "u" : 1 
#         })
#     def test_sin_vocales(self):
#         palabra = "fgh"
#         resultado = vocal_counter(palabra)
#         self.assertEqual ( resultado, {})


class TestContarVocales(unittest.TestCase):
    def test_nada(self):
        resultado = vocal_counter('zzz')
        self.assertEqual(resultado, {})

    def test_contar_a(self):
        resultado = vocal_counter('cas')
        self.assertEqual(resultado, {'a': 1})

    def test_contar_aa(self):
        resultado = vocal_counter('casa')
        self.assertEqual(resultado, {'a': 2})

    def test_contar_bese(self):
        resultado = vocal_counter('bese')
        self.assertEqual(resultado, {'e': 2})

    def test_contar_besa(self):
        resultado = vocal_counter('besa')
        self.assertEqual(resultado, {'a': 1, 'e': 1})

    def test_contar_casanova(self):
        resultado = vocal_counter('casanova')
        self.assertEqual(resultado, {'a': 3, 'o': 1})

    def test_contar_mUrciElago(self):
        resultado = vocal_counter('mUrciElago')
        self.assertEqual(resultado, {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1})


unittest.main()



