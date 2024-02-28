"""
多线程
"""
import threading
import time


# 用户下次登录时必须更改密码
def request_login_change_status(user_id, setting):
    time.sleep(1)
    setting["changePwdOnLogin"] = "Y"


# 用户不能更改该密码
def request_disable_change_status(user_id, setting):
    time.sleep(1)
    setting["disableChangePwd"] = "N"


# 并行请求接口
def thread_get_setting(user_id):
    setting = dict()

    threads = list()

    task_list = [
        request_login_change_status,
        request_disable_change_status
    ]
    for i in task_list:
        t1 = threading.Thread(target=i, args=(user_id, setting, ))
        threads.append(t1)

    # 启动所有线程
    for t in threads:
        t.start()

    # 等待所有线程执行完毕
    for t in threads:
        t.join()

    print("All tasks are done.")
    return setting


def func1():
    print("mysql任务执行完成..开始并行请求多个接口..")
    setting = thread_get_setting("123")
    print(setting)


if __name__ == '__main__':
    func1()
