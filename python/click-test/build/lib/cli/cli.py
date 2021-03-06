import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', default='Paul', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    count = count % 100
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()