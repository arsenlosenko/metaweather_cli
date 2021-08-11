import click

def print_styled_message(text, fg=None, bg=None, bold=False):
    click.echo(click.style(text, fg=fg, bg=bg, bold=bold))


def round_temp(temp):
    if temp:
        return round(float(temp))
    return temp