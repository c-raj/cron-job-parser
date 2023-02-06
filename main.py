import click
from cron_job_parser import CronJobParser

@click.command()
@click.argument("cron_expression")
def cron_parser(cron_expression):
    parser = CronJobParser()
    parser.pretty_print(cron_expression)


if __name__ == "__main__":
    cron_parser()