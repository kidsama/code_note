import ntplib

ip_address = "10.42.189.83"
ntp_client = ntplib.NTPClient()
r = ntp_client.request(ip_address, timeout=3)
print(f"连接测试ntp服务成功, ntp服务时间为{r.tx_time}")

