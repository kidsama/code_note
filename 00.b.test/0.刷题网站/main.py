import json
import pymysql
import random
from flask import Flask, render_template

# 连接 MySQL 数据库
conn = pymysql.connect(
    host='127.0.0.1',  # 主机名
    port=3306,         # 端口号，MySQL默认为3306
    user='root',       # 用户名
    password='lwx984502',  # 密码
    database='liu',   # 数据库名称
)

app = Flask(__name__)


@app.route("/xwy/random")
def index():
    result = {}
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM l_tiku ORDER BY RAND() LIMIT 1;")
            query_result = cursor.fetchone()
            if query_result:
                result["q_num"] = query_result[0]
                result["question"] = query_result[1]
                result["options"] = json.loads(query_result[2])
                result["answer"] = query_result[3]
                if query_result[4] == 1:
                    result["type"] = "判断题"
                elif query_result[4] == 3:
                    result["type"] = "多选题"
                else:
                    result["type"] = "单选题"
    except Exception as e:
        pass

    return render_template('random.html', result=result)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8003)
