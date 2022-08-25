import click

@click.command()
@click.argument('input', type=click.File('rb'))  # 指定文件为二进制读
@click.argument('output', type=click.File('wb'))  # 指定文件为二进制写
def inout(input, output):
    while True:
        chunk = input.read(1024)  # 此时 input 为文件对象，每次读入 1024 字节
        if not chunk:
            break
        output.write(chunk)  # 此时 output 为文件对象，写入上步读入的内容


if __name__ == '__main__':
    inout()