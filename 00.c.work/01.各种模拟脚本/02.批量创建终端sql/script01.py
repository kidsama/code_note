"""
@Date: 2024/4/19 上午11:09
@Author: liushaowei
@Description: 
"""
import uuid
import random

def generate_random_ipv4_address():
    ip_segments = [random.randint(1, 255) for _ in range(4)]
    return ".".join(map(str, ip_segments))

for i in range(2000):
    t_uuid = uuid.uuid4().hex
    t_hostname = f"kkk{i}.kcm39.local"
    t_devsn = str(uuid.uuid4())
    # 生成随机ip
    t_ip = generate_random_ipv4_address()

    template_sql = (
        f"INSERT INTO `terminal_host` VALUES ('{t_uuid}', '{t_hostname}', NULL, '{t_devsn}', NULL, 1, NULL, "
        f"'2023-06-05 16:17:22', 1, '{t_ip}', NULL, NULL, '笔记本', NULL, NULL, 'v10', 0, 'disabled', NULL, "
        f"NULL, NULL, '', 1, NULL);")

    print(template_sql)