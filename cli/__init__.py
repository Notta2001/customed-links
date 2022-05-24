import click

from cli.job.views import views_count



@click.group()
@click.version_option(version='1.6.3')
@click.pass_context
def cli(ctx):
    pass


cli.add_command(views_count, "views_count")