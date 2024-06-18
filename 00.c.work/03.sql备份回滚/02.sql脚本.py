import pymysql

# 连接数据库
database = "kcm_main"
conn = pymysql.connect(host='localhost', user='root', password='lwx984502', db=database)


def exec_sql():
    with conn.cursor() as cursor:
        cursor.execute("insert into server_config_dns_info_backup_20240418 select * from server_config_dns_info;")
    conn.commit()
    print("执行完成")


if __name__ == '__main__':
    exec_sql()


