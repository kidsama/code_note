import traceback
import ntplib
#
# def check_ntp_service(ip_address):
#     try:
#         ntp_client = ntplib.NTPClient()
#         r = ntp_client.request(ip_address)
#         print(f"连接测试ntp服务成功, ntp服务时间为{r.tx_time}")
#         return True
#     except Exception as e:
#         traceback.print_exc()
#         return False

def check_ntp_service(ip_address):
    check_flag = False
    for i in range(3):
        try:
            ntp_client = ntplib.NTPClient()
            r = ntp_client.request(ip_address, timeout=3)
            print(f"连接测试ntp服务成功, ntp服务时间为{r.tx_time}")
            check_flag = True
            break
        except Exception as e:
            traceback.print_exc()
    return check_flag

check_ntp_service("ntp.tencent.com")