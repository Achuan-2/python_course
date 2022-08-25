import click

def get_commit_message():
    message = click.edit()
    print(message)



if __name__ == '__main__':
    get_commit_message()
