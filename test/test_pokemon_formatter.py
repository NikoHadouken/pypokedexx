import unittest

from pypokedexx.formatter import PokemonFormatter


class TestPokemonFormatter(unittest.TestCase):
    def test_only_returns_correct_keys(self):
        formatter = PokemonFormatter()
        pokemon = {
            'id': '25',
            'name': 'Pikachu',
            'weight': 60,
            'abilities': [],
        }
        res = formatter.format(pokemon)
        self.assertFalse("abilities" in res)
