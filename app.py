import click
from collections import namedtuple
from commands import cmd

Options = namedtuple('Options', ['opt1', 'opt2'])

@click.group()
@click.pass_context
@click.option('--opt1', required=True, help='opt1')
@click.option('--opt2', required=True, help='opt2')
def entry_point(ctx, opt1, opt2):
    ctx.obj = Options(opt1, opt2)

entry_point.add_command(cmd.cmd)

if __name__ == "__main__":
    entry_point()
