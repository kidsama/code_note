#
# # import time
# # from datetime import datetime, date, timedelta
# #
# # cron = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(1692144000000 / 1000)))
# # print(cron, type(cron))
# #
# # aaa = datetime.strptime(cron, "%Y-%m-%d %H:%M:%S")
# # print(aaa, type(aaa))
# #
# #
# #
# # # import datetime
# #
# # # t = datetime.datetime.now()
# # # print(t, type(t))
# # # # 当前日期
# # # # d1 =t.strftime('%Y-%m-%d %H:%M:%S')
# # # # 7天后
# # # d2 =(t+datetime.timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
# # # print(d2, type(d2))
# #
# # d1 = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
# # print(d1, type(d1))
# #
# # d2 = datetime.strptime(d1, "%Y-%m-%d %H:%M:%S")
# # print(d2, type(d2))
#
#
# print("=========")
# import datetime
#
# s_time = "2930-06-05T16:00:00Z"
# time_obj = datetime.datetime.strptime(
#                     s_time, "%Y-%m-%dT%H:%M:%SZ"
#                 )
# print(time_obj, type(time_obj))
#
# aaa = time_obj + datetime.timedelta(hours=8)
# print(aaa, type(aaa))
#
# now = datetime.datetime.now()
# print(now, type(now))
# # result = now + datetime.timedelta(hours=8)
# #
# # print(result)

import datetime

def get_default_time():
    try:
        max_password_expiration = 5000

        # s_time = "2930-06-05T16:00:00Z"
        #

        aaa = datetime.datetime.now() + datetime.timedelta(seconds=max_password_expiration)
        time_obj = aaa.strftime("%Y-%m-%dT%H:%M:%S+08:00")
        print(time_obj, type(time_obj))


    except Exception as e:
        import traceback
        traceback.print_exc()

get_default_time()
