"""
@Date: 2024/5/11 下午3:00
@Author: liushaowei
@Description: 
"""
import socket

# web服务器 hpfdkylin.hpf.gov.hk  10.42.189.83/kylincloud@123.
# 接收日志的服务器  10.42.4.226/kylin/hjkl7890
# 同网段服务器 10.42.4.227/kylin/qwer1234

aaa = """
tail -f /var/log/syslog
"""


def send_rsyslog(msg):
    set_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        set_sock.sendto(msg.encode(), ("10.42.4.226", 514))
        print("发送成功")
    except socket.error as e:
        print("socket error")
    except Exception as e1:
        import traceback
        traceback.print_exc()
    set_sock.close()

send_rsyslog("xxxxxxxxxxxxxxx")



