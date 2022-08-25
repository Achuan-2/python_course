import click


@click.command()
@click.option('-s', '--string', default='World',help="This is the thing that is greeted")
@click.option('-n', '--number', default=1, help="This is the number of times to greet")
@click.argument('output', type=click.File('w'), default='-',required=False)
def cli(string,number,output):
    """This scripts greets you."""
    for x in range(number):
        click.echo(f'Hello {string}', file=output)

