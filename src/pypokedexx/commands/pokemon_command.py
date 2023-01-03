from pypokedexx.api.poke_api import PokeApi
from pypokedexx.formatter import PokemonFormatter
from ..utils import to_json
from ..logger import Logger


class PokemonCommand:
    def __init__(self, logger: Logger):
        self._logger = logger
        self._api = PokeApi()
        self._formatter = PokemonFormatter()

    def get(self, name):
        pokemon = self._api.get_pokemon(name)

        if pokemon is None:
            self._logger.error("Pokemon not found")
        else:
            formatted = self._formatter.format(pokemon)
            self._logger.log(to_json(formatted))
