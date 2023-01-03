import click

from .__version__ import __version__
from .commands.pokemon_command import PokemonCommand
from .logger import Logger


def _bootstrap():
    logger = Logger()
    command = PokemonCommand(logger=logger)
    return command


@click.group()
@click.pass_context
def cli(ctx):
    """Pokedexx CLI"""
    cmd = _bootstrap()
    ctx.obj = cmd


@cli.command(name="pokemon:get")
@click.argument('name')
@click.pass_obj
def get_pokemon(cmd: PokemonCommand, name: str):
    """Get pokemon by name"""
    click.echo(f"pokemon:get {name}")
    cmd.get(name)


@cli.command(name="version")
def get_version():
    """Get Pypokedexx CLI version"""
    click.echo(__version__)


def main():
    cli()  # pylint: disable=no-value-for-parameter
