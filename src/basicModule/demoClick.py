import click
 
@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
def input_password(password):
    click.echo('password: %s' % password)

if __name__ == '__main__':
    input_password()