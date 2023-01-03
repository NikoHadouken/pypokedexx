
class PokemonFormatter:

    def format(self, pokemon: dict):
        pokemon = {k: v for k, v in pokemon.items() if k in [
            'id', 'name', 'weight']}
        return pokemon
