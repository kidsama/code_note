import time
import threading


# 定义一个函数，作为线程的主体功能
def do_something():
    # 在这里编写你要执行的功能
    print("开始执行...")
    time.sleep(3)
    print("执行结束")




# 在这里继续执行主任务
if __name__ == '__main__':
    print("==========1==========")
    # 创建线程对象
    thread = threading.Thread(target=do_something)

    # 启动线程
    thread.start()
    print("==========2==========")