import click

@click.command()
@click.argument('mode', type=click.Choice(['read-only', 'read-write']))
def hello(mode):
    click.echo(mode)


if __name__ == '__main__':
    hello()