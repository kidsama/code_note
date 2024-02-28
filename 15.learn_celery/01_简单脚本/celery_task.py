
import celery
import time
backend = 'redis://:Kcm.2022@127.0.0.1:6379/1'     # 设置Redis的1数据库来存放结果
broker = 'redis://:Kcm.2022@127.0.0.1:6379/2'      # 设置Redis的2数据库来存放消息中间件
cel = celery.Celery('test', backend=backend, broker=broker)
# 参数说明：第一个是Celery的名字，Celery和哪个项目相关就命名哪个
# 后面两个关键字参数用于指定消息中间件和结果存放位置。


@cel.task
def send_email(name):
    print("向%s发送邮件..." % name)
    time.sleep(5)
    print("向%s发送邮件完成" % name)
    return "ok"


@cel.task
def send_msg(name):
    print("向%s发送短信..." % name)
    time.sleep(5)
    print("向%s发送短信完成" % name)
    return "ok"
