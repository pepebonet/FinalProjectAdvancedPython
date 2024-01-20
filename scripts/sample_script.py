import click

@click.group(help="Test different levels of click")
def cli():
    pass

@cli.command(short_help='Function to say hello') # Notice I am not puting click anymore but cli
@click.option('-pn', '--print_name', default='Pepe', help='Name to print')
def say_name(print_name):
    """
    Function to say hello
    """
    print(f'Hello {print_name}')

@cli.command(short_help='Function to say hello') # Notice I am not puting click anymore but cli
@click.option('-pa', '--print_age', default=29, help='Say years old')
def say_age(print_age):
    """
    Function to say age
    """
    print(f'I am {print_age} years old')

if __name__ == "__main__":
    cli()
