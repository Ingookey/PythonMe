# coding:utf-8

import click
from basicModule import *

@click.command()
@click.option('--times', default = 2)
@click.option('--password', prompt = True, hide_input = True, confirmation_prompt = True)
def input_password(times, password):
    print('<input_password>', time.localtime())
    for _ in range(times):
        click.echo('Which times: %s' % _)
    click.echo('Input Password: %s' % password)

if __name__ == '__main__':
    input_password()
