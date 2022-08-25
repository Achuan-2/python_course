import click

@click.command()
@click.option('-s', '--strin', 'strin',default='2')
def echo(strin):
    click.echo(strin)

if __name__ == '__main__':
    echo()