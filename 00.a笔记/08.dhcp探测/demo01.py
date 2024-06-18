"""
@Date: 2024/5/9 下午3:12
@Author: liushaowei
@Description: 
"""

import socket
import time

def udp_port_test(ip, port, retries=3, timeout=3):
    for _ in range(retries):
        try:
            udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_socket.settimeout(timeout)

            # 发送数据
            udp_socket.sendto(b'hello', (ip, port))

            # 尝试接收数据，如果端口开放，应该能收到响应
            data, addr = udp_socket.recvfrom(1024)
            print(f"UDP port {port} is open: {data.decode()}")

            # 如果收到响应，我们可以假设端口是开放的
            break
        except socket.timeout:
            print(f"UDP port {port} seems to be closed or not responding.")
        finally:
            udp_socket.close()
            time.sleep(1)  # 等待1秒再重试，避免过于频繁的请求

    if _ == retries - 1:
        print(f"UDP port {port} is consistently not responding after {retries} attempts.")

if __name__ == '__main__':
    udp_port_test('10.42.189.7', 67)