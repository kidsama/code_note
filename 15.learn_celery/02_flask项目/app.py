import time
from flask import Flask, jsonify
from celery import Celery
from celery.result import AsyncResult
from celery import states

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://:Kcm.2022@localhost:6379/1'
app.config['CELERY_RESULT_BACKEND'] = 'redis://:Kcm.2022@localhost:6379/2'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)



@app.route('/status/<task_id>', methods=['GET'])
def check_task_status(task_id):
    task = AsyncResult(id=task_id, app=celery)

    if task.state == 'PENDING':
        return jsonify({"message": "任务尚未开始"})
    elif task.state == 'SUCCESS':
        return jsonify({"message": "任务已完成", "result": task.result})
    elif task.state in states.READY_STATES:  # 包括 'RETRY', 'FAILURE' 等状态
        return jsonify({"message": f"任务状态：{task.state}", "result": task.info})
    else:
        return jsonify({"message": "任务正在进行"})


@celery.task(bind=True)
def long_running_task(self):
    # 耗时10分钟的函数
    print("开始执行")
    time.sleep(10)  # 示例用法，实际替换成你的业务逻辑
    print("执行完成")
    return "执行完成"


@app.route('/long')
def trigger_long_running():
    task = long_running_task.apply_async()
    return jsonify({"message": "处理完成，请稍后查看数据状态", "task_id": task.id})


if __name__ == '__main__':
    app.run(debug=True)


# 启动celery
# celery -A app.celery worker --loglevel=info
