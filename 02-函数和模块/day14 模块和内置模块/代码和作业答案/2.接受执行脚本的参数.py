import sys


print(sys.argv)  # ['2.接受执行脚本的参数.py', 'achuan', 'pic']


# 例如，请实现下载图片的一个工具。

def download_image(url):
    print("下载图片", url)


def run():
    # 接受用户传入的参数
    url_list = sys.argv[1:]
    for url in url_list:
        download_image(url)


if __name__ == '__main__':
    #  python 2.接受执行脚本的参数.py achuan pic
    run()
    
