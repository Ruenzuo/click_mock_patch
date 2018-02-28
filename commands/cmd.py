import click

from helpers.helper import do_something_useful

@click.command(name = "cmd", short_help="cmd")
@click.pass_context
def cmd(ctx):
    opt1 = ctx.obj.opt1
    opt2 = ctx.obj.opt2
    click.echo("Options are: {} and {}".format(opt1, opt2))
    do_something_useful(opt1, opt2)

