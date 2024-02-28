import sys
sys.path.append('/home/www-data/flask')
# 3.8及以下版本把myapi.config.mysql_connect 替换为myapi.resources.mysql_connect
from myapi.config.mysql_connect import KCM
import MySQLdb
db = MySQLdb.connect(host=KCM.HOST, user=KCM.USERNAME, passwd=KCM.PASSWORD, db="kcm", charset='utf8')
print('mysql连接：{}'.format(db))
cursor = db.cursor()
def select(sql):
    cursor.execute(sql)
    result_list = cursor.fetchall()
    return result_list

result = select("select * from area;")

