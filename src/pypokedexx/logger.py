import click


class Logger:
    def log(self, message):
        click.echo(message)

    def error(self, message):
        click.echo(message, err=True, color=True)
