from requests import request


class PokeApi:
    """
    Wrapper Class for PokeApi
    https://pokeapi.co/
    """
    BASE_URL = 'https://pokeapi.co/api/v2'

    def get_pokemon(self, name: str):
        """Get pokemon by name or id"""
        res = request(
            'GET',
            f"{self.BASE_URL}/pokemon/{name}",
            timeout=30,
        )

        if res.status_code == 404:
            return None

        if res.status_code >= 400 and res.status_code <= 600:
            raise Exception(f"error response {res.status_code}")

        return res.json()
