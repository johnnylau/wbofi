import click

@click.command()
@click.option('--userid', help="set userid which u wanna search")
@click.option('--photo', default=True, help="set if you wanna download user's photo")
@click.option('--album', default=False, help="whether download user's photo album's photo")
@click.option('--flist', default=False, help="whether get follow list of this user")
@click.option('--ferlist', default=False, help="whether get follower list of this user")
@click.option('--elist', default=False, help="whether get follow each-other list of user")
@click.option('--rflist', default=False, help="recurcive all user of follow list and get their user name and user's photo")