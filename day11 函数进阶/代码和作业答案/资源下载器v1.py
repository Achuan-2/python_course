
import requests
import os


COLOR = {
    'blue': '\033[94m',
    'yellow': '\033[93m',
    'red': '\033[91m',
    'green': '\033[92m',
    'cyan': '\033[96m',
    'magenta': '\033[95m',
    'white': '\033[97m',
    'end': '\033[0m',
}

SELECTED_IMAGE_SET = set()  # 已下载图片ID（序号）
SELECTED_VIDEO_SET = set()
SELECTED_NBA_SET = set()

def main():
    print(COLOR['blue']+"欢迎来到资源下载器软件".center(20, '！')+COLOR['end'])

    func_dict = {
        "1": download_huaban,
        "2": download_douyin,
        "3": download_nba
    }
    while True:
        print("\n专区列表".center(20, '*'))
        print("""
        1.花瓣网图片专区
        2.抖音短视频专区
        3.NBA锦集专区
        """)
        print("*".center(24, '*'))
        choice = input(COLOR['green']+"请输入你要进入的专区编号:"+COLOR['end'])

        func = func_dict.get(choice)
        if not func:
            print(COLOR['red']+"输入有误"+COLOR['end'])
            continue
        else:
            func()




def download_huaban():
    total_image_dict = {
        "1": ("吉他男神", "https://hbimg.huabanimg.com/51d46dc32abe7ac7f83b94c67bb88cacc46869954f478-aP4Q3V"),
        "2": ("漫画美女", "https://hbimg.huabanimg.com/703fdb063bdc37b11033ef794f9b3a7adfa01fd21a6d1-wTFbnO"),
        "3": ("游戏地图", "https://hbimg.huabanimg.com/b438d8c61ed2abf50ca94e00f257ca7a223e3b364b471-xrzoQd"),
        "4": ("alex媳妇", "https://hbimg.huabanimg.com/4edba1ed6a71797f52355aa1de5af961b85bf824cb71-px1nZz"),
    }
    while True:
        ####打印可下载信息####
        # 1.吉他男神; 2.漫画美女; 3.游戏地图; 4.alex媳妇
        text_list = []
        for num, item in total_image_dict.items():
            if num in SELECTED_IMAGE_SET:
                continue
            data = f"{num}.{item[0]}"
            text_list.append(data)
        if text_list:
            text = "; ".join(text_list)
            print((COLOR['cyan']+f"可下载列表：{text}"+COLOR['end']))
        else:
            print(COLOR['yellow']+"无可下载选项。已全部下载"+COLOR['end'])

        ####选择下载项####
        index = input(COLOR['green']+"请输入要选择的序号(Q/q退出）："+COLOR['end'])
        # 输入Q/q返回上一步
        if index.upper() == "Q":
            return
        # 已下载序号不能重复选择
        if index in SELECTED_IMAGE_SET:
            print(COLOR['red']+"已下载，无法再继续下载，请重新选择！"+COLOR['end'])
            continue
        group = total_image_dict.get(index)
        if not group:
            print(COLOR['red']+"序号不存在，请重新选择"+COLOR['end'])
            continue

        ####下载####
        # 下载图片
        mkdir("pictures")
        file_path = "pictures/{}.png".format(group[0])

        download(file_path, group[1])
        # 已下载集合添加索引
        SELECTED_IMAGE_SET.add(index)


def download_douyin():
    total_video_dict = {
        "1": {"title": "东北F4模仿秀",
              'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"},
        "2": {"title": "卡特扣篮",
              'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"},
        "3": {"title": "罗斯mvp",
              'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg"},
    }

    while True:
        ####打印可下载信息####
        # 1.东北F4模仿秀; 2.卡特扣篮; 3.罗斯mvp;
        text_list = []
        for num, item in total_video_dict.items():
            if num in SELECTED_VIDEO_SET:
                continue
            data = f"{num}.{item['title']}"
            text_list.append(data)
        if text_list:
            text = "; ".join(text_list)
            print((COLOR['cyan']+f"可下载列表：{text}"+COLOR['end']))
        else:
            print(COLOR['yellow']+"无可下载选项。已全部下载"+COLOR['end'])

        ####选择下载项####
        index = input(COLOR['green']+"请输入要选择的序号(Q/q退出）："+COLOR['end'])
        # 输入Q/q返回上一步
        if index.upper() == "Q":
            return
        # 已下载序号不能重复选择
        if index in SELECTED_VIDEO_SET:
            print(COLOR['red']+"已下载，无法再继续下载，请重新选择！"+COLOR['end'])
            continue
        group = total_video_dict.get(index)
        if not group:
            print(COLOR['red']+"序号不存在，请重新选择"+COLOR['end'])
            continue

        ####下载####
        # 下载视频
        mkdir("douyin")
        file_path = "douyin/{}.mp4".format(group['title'])

        download(file_path, group['url'])
        # 已下载集合添加索引
        SELECTED_VIDEO_SET.add(index)


def download_nba():
    total_nba_dict = {
        "1": {"title": "威少奇才首秀三双",
              "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300fc20000bvi413nedtlt5abaa8tg&ratio=720p&line=0"},
        "2": {"title": "塔图姆三分准绝杀",
              "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0d00fb60000bvi0ba63vni5gqts0uag&ratio=720p&line=0"}

    }

    while True:
        ####打印可下载信息####
        # 1.东北F4模仿秀; 2.卡特扣篮; 3.罗斯mvp;
        text_list = []
        for num, item in total_nba_dict.items():
            if num in SELECTED_NBA_SET:
                continue
            data = f"{num}.{item['title']}"
            text_list.append(data)
        if text_list:
            text = "; ".join(text_list)
            print((COLOR['cyan']+f"可下载列表：{text}"+COLOR['end']))
        else:
            print(COLOR['yellow']+"无可下载选项。已全部下载"+COLOR['end'])

        ####选择下载项####
        index = input(COLOR['green']+"请输入要选择的序号(Q/q退出）："+COLOR['end'])
        # 输入Q/q返回上一步
        if index.upper() == "Q":
            return
        # 已下载序号不能重复选择
        if index in SELECTED_NBA_SET:
            print(COLOR['red']+"已下载，无法再继续下载，请重新选择！"+COLOR['end'])
            continue
        group = total_nba_dict.get(index)
        if not group:
            print(COLOR['red']+"序号不存在，请重新选择"+COLOR['end'])
            continue

        ####下载####
        # 下载视频
        mkdir("nba")
        file_path = "nba/{}.mp4".format(group['title'])

        download(file_path, group['url'])
        # 已下载集合添加索引
        SELECTED_NBA_SET.add(index)


def download(file_path, url):
    res = requests.get(
        url=url,
        headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 FS"
        }
    )
    with open(file_path, mode='wb') as f:
        f.write(res.content)
    print(f"已下载{file_path}")


def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

if __name__ == '__main__':
    main()
