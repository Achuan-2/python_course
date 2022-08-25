import click


@click.command()
@click.option('-v', '--verbose', count=True)
def log(verbose):
    click.echo(f'Verbosity: {verbose}')


if __name__ == '__main__':
    log()