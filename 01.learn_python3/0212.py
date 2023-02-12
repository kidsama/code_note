"""
字段映射
热爆沸(1/5/6) -> 热(1)
新(3) -> 新(3)
荐商(2/4) -> 商(4)
其它 -> 0

要求
新(3)最多能有1个
热(1)最多能有2个
新加热(1+3)最多能有两个
商(4)最多能有1个
"""

word_data = [
    {"id": 1, "icon": 1, "word": "热"},
    {"id": 2, "icon": 2, "word": "荐"},
    {"id": 3, "icon": 3, "word": "新"},
    {"id": 4, "icon": 4, "word": "商"},
    {"id": 5, "icon": 5, "word": "爆"},
    {"id": 6, "icon": 6, "word": "沸"},
    {"id": 7, "icon": 3, "word": "新"},
    {"id": 8, "icon": 4, "word": "商"},
    {"id": 9, "icon": 5, "word": "爆"}
]


def ppprint(data_info):
    print("============")
    for i in data_info:
        print(i)
    print("============")


def make_simulator():
    simulator_data = []
    word_lib = [
        {"icon": 0, "word": "无图标0"},
        {"icon": 0, "word": "无图标0"},
        {"icon": 1, "word": "热1"},
        {"icon": 2, "word": "荐2 -> 商4"},
        {"icon": 3, "word": "新3"},
        {"icon": 3, "word": "新3"},
        {"icon": 3, "word": "新3"},
        {"icon": 3, "word": "新3"},
        {"icon": 4, "word": "商4"},
        {"icon": 5, "word": "爆5 -> 热1"},
        {"icon": 6, "word": "沸6 -> 热1"},
        {"icon": 5, "word": "爆5 -> 热1"},
        {"icon": 6, "word": "沸6 -> 热1"},
        {"icon": 5, "word": "爆5 -> 热1"},
        {"icon": 6, "word": "沸6 -> 热1"},
        {"icon": 7, "word": "独家7 -> 无图标0"},
        {"icon": 8, "word": "首发8 -> 无图标0"},
        {"icon": 9, "word": "直播9 -> 无图标0"},
        {"icon": 10, "word": "热度上升10"},
        {"icon": 11, "word": "热度下降11"},
        {"icon": 12, "word": "置顶12"},
        {"icon": 13, "word": "专题13 -> 无图标0"}
    ]
    import random
    import copy
    for i in range(50):
        num = random.randint(0, 13)
        this_word = copy.deepcopy(word_lib[num])
        this_word["id"] = i + 1
        simulator_data.append(this_word)

    return simulator_data


# 1.转换图标
def change_icon_new(data_info):
    for item in data_info:
        if item.get("icon") in [1, 5, 6]:
            item["icon_new"] = 1
        elif item.get("icon") in [2, 4]:
            item["icon_new"] = 4
        elif item.get("icon") in [3, 10, 11, 12]:
            item["icon_new"] = item.get("icon")
        else:
            item["icon_new"] = 0


# 2.只留一个商的词条
def remove_redundant_shang(data_info):
    new_data_info = []
    is_exist_in_this_page = False
    for item in data_info:
        if item.get("icon_new") == 4:
            if not is_exist_in_this_page:
                new_data_info.append(item)
                is_exist_in_this_page = True
        else:
            new_data_info.append(item)
        if len(new_data_info) % 7 == 0:
            is_exist_in_this_page = False
    return new_data_info


# 3.1 计算前7条中需要保留的爆热沸各自的数量
def cal_three_icon_count(data_info):
    first_page_data = data_info[:7]
    icon_list = [i.get("icon") for i in first_page_data]
    bao_count = icon_list.count(5)
    fei_count = icon_list.count(6)
    re_count = icon_list.count(1)
    xin_count = icon_list.count(3)
    need_bao_count = 0
    need_fei_count = 0
    need_re_count = 0
    need_xin_count = 0
    if bao_count >= 2:
        # 只要前两个爆即可
        need_bao_count = 2
    elif bao_count == 1:
        # 再取 1个沸
        need_bao_count = 1
        if fei_count >= 1:
            need_fei_count = 1
        else:
            # 没有沸, 取1个热
            if re_count >= 1:
                need_re_count = 1
    else:
        # 没有爆, 从沸开始判断
        if fei_count >= 2:
            # 只要前两个沸即可
            need_fei_count = 2
        elif fei_count == 1:
            need_fei_count = 1
            # 再取一个热
            if re_count >= 1:
                need_re_count = 1
        else:
            # 没有沸, 留两个热
            if re_count >= 2:
                # 只要前两个热
                need_re_count = 2
            else:
                # 热图标符合要求，无需处理
                need_re_count = re_count
    total_re_count = need_bao_count + need_fei_count + need_re_count
    if total_re_count >= 2:
        # 热的图标已经够2个, 不需要新图标
        need_xin_count = 0
    elif total_re_count == 1:
        # 热图标只有1个,还需要1个新
        if xin_count >= 1:
            need_xin_count = 1
    else:
        # 没有热，只要第一个新
        if xin_count >= 1:
            need_xin_count = 1
    return need_bao_count, need_fei_count, need_re_count, need_xin_count


# 3.只留最多两个图标
def remain_two_icon(data_info):
    """
    其中 热>新
    热的逻辑: 最多留两个 爆>沸>热  5>6>1
    新的逻辑: 最多留1个
    :param data_info:
    :return:
    """
    need_bao_count, need_fei_count, need_re_count, need_xin_count = cal_three_icon_count(data_info)
    for item in data_info:
        if item.get("icon") == 5:
            if need_bao_count > 0:
                need_bao_count = need_bao_count - 1
                continue
            else:
                item["icon_new"] = 0
        elif item.get("icon") == 6:
            if need_fei_count > 0:
                need_fei_count = need_fei_count - 1
                continue
            else:
                item["icon_new"] = 0
        elif item.get("icon") == 1:
            if need_re_count > 0:
                need_re_count = need_re_count - 1
                continue
            else:
                item["icon_new"] = 0
        elif item.get("icon") == 3:
            if need_xin_count > 0:
                need_xin_count = need_xin_count - 1
                continue
            else:
                item["icon_new"] = 0
        else:
            continue


# n.最后一步 icon值覆盖并删除icon_new字段
def replace_icon_value(data_info):
    for item in data_info:
        item["icon"] = item.get("icon_new")
        item.pop("icon_new")


# 重组数据
def rebuild_data(data_info):
    # 1.图标映射
    change_icon_new(data_info)
    # 2.只留一个商的词条
    data_info1 = remove_redundant_shang(data_info)

    # 3.只留两个图标(新+热)
    remain_two_icon(data_info1)

    # n.最后一步 icon值覆盖并删除icon_new字段
    replace_icon_value(data_info1)

    return data_info1


# 校验数据
def check_data(data_info):
    page_info = data_info[:7]
    only_icon = [0, 1, 3, 4, 10, 11, 12]
    icon_list = [i.get("icon") for i in page_info]

    if len(list(set(icon_list) - set(only_icon))) > 0:
        print("存在未映射的图标")
        return False

    re_count = icon_list.count(1)
    xin_count = icon_list.count(3)
    shang_count = icon_list.count(4)
    if re_count + xin_count + shang_count > 3:
        print("总图标超过3个")
        return False
    if re_count + xin_count > 2:
        print("新和热 图标超过2个")
        return False
    if xin_count > 1:
        print("新 图标超过1个")
        return False

    if re_count > 2:
        print("热 图标超过2个")
        return False

    if shang_count > 1:
        print("商 图标超过1个")
        return False
    return True


if __name__ == '__main__':
    for i in range(10000):
        # 造数据
        simulator_data = make_simulator()
        # print("======原始数据==========")
        # ppprint(simulator_data[:10])
        # 处理数据
        new_word_data = rebuild_data(simulator_data)
        # print("======处理完的数据==========")
        # ppprint(new_word_data[:7])
        # 检验数据
        check_result = check_data(new_word_data)
        if check_result:
            pass
        else:
            print("======原始数据==========")
            ppprint(simulator_data[:10])
            print("======处理完的数据==========")
            ppprint(new_word_data[:7])
            print("校验失败")
