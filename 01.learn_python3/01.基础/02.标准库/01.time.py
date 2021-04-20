# @Time : 2021/1/15 17:51
# @Author : liu
# @Notes :

import time

# time.time 万物基于时间戳
now_time = time.time()
print(now_time)

# time.localtime 时间元组,不加参数则为当前时间
print(time.localtime(now_time))
print(time.localtime())

# time.strftime 格式化时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

