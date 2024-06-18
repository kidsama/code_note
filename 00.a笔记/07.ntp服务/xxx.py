"""
@Date: 2024/4/8 下午2:14
@Author: liushaowei
@Description: 
"""

import socket
import time

def is_udp_port_open(host, port, timeout=2):
    """
    检测给定主机（IP 地址）上的指定 UDP 端口是否通畅。

    参数:
        host (str): 目标主机的 IP 地址。
        port (int): 待检测的 UDP 端口号。
        timeout (float, optional): 等待响应的超时时间（秒）。默认为 2 秒。

    返回:
        bool: 如果端口开放并收到响应，则返回 True，否则返回 False。
    """
    try:
        # 创建一个 UDP 套接字
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 设置套接字超时时间
        sock.settimeout(timeout)

        # 向目标主机和端口发送一个空的数据包
        sock.sendto(b'', (host, port))

        # 尝试接收响应
        sock.recvfrom(1)  # 期望接收一个字节，实际上我们只关心是否能接收到任何数据

        # 如果能成功接收数据，说明端口是开放的
        return True

    except (socket.timeout, socket.error) as e:
        # 超时或发生其他网络错误，认为端口不可达或未开放
        print(f"检测UDP端口时发生错误：{e}")
        return False

    finally:
        # 关闭套接字
        sock.close()

# 使用示例
target_host = '10.42.5.11'
target_port = 123
is_port_open = is_udp_port_open(target_host, target_port)
print(f"UDP端口 {target_port} 是否开放：{is_port_open}")
