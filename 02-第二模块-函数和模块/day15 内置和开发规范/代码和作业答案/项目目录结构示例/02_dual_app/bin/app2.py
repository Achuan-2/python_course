import os
import sys

# 添加上级目录到环境变量
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.handler import start

if __name__ == '__main__':
    start()
