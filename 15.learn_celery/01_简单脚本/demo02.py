from celery.result import AsyncResult
from celery_task import cel
async_result=AsyncResult(id="8aa517a2-65d1-4be3-bfed-c08285a505ad", app=cel)
if async_result.successful():
    result = async_result.get()
    print(result)
    # result.forget() # 将结果删除
elif async_result.failed():
    print('执行失败')
elif async_result.status == 'PENDING':
    print('任务等待中被执行')
elif async_result.status == 'RETRY':
    print('任务异常后正在重试')
elif async_result.status == 'STARTED':
    print('任务已经开始被执行')