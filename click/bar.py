import time
import click

all_the_users_to_process = ['a', 'b', 'c']


def modify_the_user(user):
    time.sleep(0.5)


with click.progressbar(all_the_users_to_process) as bar:
    for user in bar:
        modify_the_user(user)
