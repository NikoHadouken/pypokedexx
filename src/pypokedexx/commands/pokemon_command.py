from pypokedexx.api.poke_api import PokeApi
from ..utils import to_json
from ..logger import Logger


class PokemonCommand:
    def __init__(self, logger: Logger):
        self._logger = logger
        self._api = PokeApi()

    def get(self, name):
        pokemon = self._api.get_pokemon(name)

        if pokemon is None:
            self._logger.error("Pokemon not found")
        else:
            pokemon = {k: v for k, v in pokemon.items() if k in [
                'id', 'name', 'weight']}
            self._logger.log(to_json(pokemon))
