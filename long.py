import click

def _generate_output():
    for idx in range(50000):
        yield "Line %d\n" % idx

@click.command()
def less():
    click.echo_via_pager(_generate_output())


if __name__ == '__main__':
    less()1111
