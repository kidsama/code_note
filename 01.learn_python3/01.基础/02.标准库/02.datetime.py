'''
今天 today = datetime.date.today()
昨天 yesterday = today - datetime.timedelta(days=1)
上个月 last_month = today.month - 1 if today.month - 1 else 12
当前时间戳 time_stamp = time.time()
时间戳转datetime datetime.datetime.fromtimestamp(time_stamp)
datetime转时间戳 int(time.mktime(today.timetuple()))
datetime转字符串 today_str = today.strftime("%Y-%m-%d")
字符串转datetime today = datetime.datetime.strptime(today_str, "%Y-%m-%d")
补时差 today + datetime.timedelta(hours=8)

'''