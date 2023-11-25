from typing import List


# 判断a中的组织，是否完全被b管辖(a.startswith(b))
def check_total_contain_2(area_paths_a: List[str], area_paths_b: List[str]) -> bool:
    if None in area_paths_b:
        return False
    for path_a in area_paths_a:
        if path_a is not None and all(
            not path_a.startswith(f"{path_b}") for path_b in area_paths_b
        ):
            return False
    return True


def check_total_contain_3(area_paths_a: List[str], area_paths_b: List[str]) -> bool:
    if None in area_paths_b:
        return False
    for path_a in area_paths_a:
        if all(not path_a.startswith(path_b) for path_b in area_paths_b):
            return False
    return True


def check_total_contain_4(area_paths_a: List[str], area_paths_b: List[str]) -> bool:
    if None in area_paths_b:
        return False
    for path_a in area_paths_a:
        if path_a is not None and all(
                not f"{path_a},".startswith(f"{path_b},") for path_b in area_paths_b
        ):
            return False
    return True


# 判断a中的组织，是否完全被b管辖(a.startswith(b))
def check_total_contain_1(area_path_list_a, area_path_list_b):
    for i in area_path_list_a:
        for j in area_path_list_b:
            if j is None:
                return False
            # 未分配组织的用户为全部用户的子用户
            if i is not None and not i.startswith(f"{j},"):
                return False
    return True

def check_total_contain_5(area_paths_a: List[str], area_paths_b: List[str]) -> bool:
    if None in area_paths_b:
        return False
    for path_a in area_paths_a:
        if path_a is not None and all(
                not f"{path_a},".startswith(f"{path_b},") for path_b in area_paths_b
        ):
            return False
    if check_total_equal(area_paths_a, area_paths_b):
        return False
    return True

def check_total_equal(area_path_list_a, area_path_list_b):
    set1 = set(area_path_list_a)
    set2 = set(area_path_list_b)
    if set1.difference(set2) or set2.difference(set1):
        return False
    else:
        return True

a = [',1,23', ',1,46', ',1,19']
b = [',1,23', ',1,46', ',1']

print("最早我的x", check_total_contain_1(a, b))
print("张一夫的x", check_total_contain_2(a, b))
print("张一夫，x", check_total_contain_3(a, b))
print("张一夫,,x", check_total_contain_4(a, b))
print("张一夫,,v", check_total_contain_5(a, b))
