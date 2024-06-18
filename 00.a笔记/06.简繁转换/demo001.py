import zhconv
from opencc import OpenCC

def hans_2_hant(hans_str: str):
    converter = OpenCC("s2hk")
    return converter.convert(hans_str)


# 繁体转简体
def hant_2_hans(hant_str: str):
    converter = OpenCC("t2s")
    return converter.convert(hant_str)


# print(hans_2_hant("每个星期六下午三点{}豆腐干豆腐"))
#
# cron_tip = "2024-03-21 20:01:20"
# file_name = "定重下"
# user_name = "admin"
# name = "时置码，发时间：{}，重置名称：{}，创建人：{}"
#
# print(hans_2_hant(name).format(cron_tip, file_name, user_name))

print(hans_2_hant("未分组 总署 奇安信浏览器 普通 离线 操作系统版本 硬盘 未收到 完成 批量添加用户 已完成 文件"))
print("未分组 总署 奇安信浏览器 普通 离线 操作系统版本")