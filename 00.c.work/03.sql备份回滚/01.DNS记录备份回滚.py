"""
@Date: 2024/4/18 上午9:16
@Author: liushaowei
@Description: 
"""

import json
import pymysql

# 连接数据库
database = "kcm_main"
conn = pymysql.connect(host='localhost', user='root', password='lwx984502', db=database)


# 还原4张表
def reset_2_tables():
    with conn.cursor() as cursor:
        # 删除task表
        cursor.execute("drop table if exists server_config_dns_title;")
        cursor.execute("drop table if exists server_config_dns_info;")
        # 复制表结构
        cursor.execute("create table if not exists server_config_dns_title like server_config_dns_title_backup_20240418;")
        cursor.execute("create table if not exists server_config_dns_info like server_config_dns_info_backup_20240418;")
        # 复制表数据
        cursor.execute("insert into server_config_dns_title select * from server_config_dns_title_backup_20240418;")
        cursor.execute("insert into server_config_dns_info select * from server_config_dns_info_backup_20240418;")
    conn.commit()
    print("回滚完成")


# 备份2张表
def backup_2_tables():
    with conn.cursor() as cursor:
        backup_ready_sql1 = "select 1 from information_schema.tables where table_name='server_config_dns_info_backup_20240418' and TABLE_SCHEMA=%s;"
        cursor.execute(backup_ready_sql1, [database])
        res1 = cursor.fetchone()
        if res1:
            print("备份表server_config_dns_info已存在，不再进行备份..")
        else:
            # 复制表结构
            cursor.execute("create table server_config_dns_info_backup_20240418 like server_config_dns_info;")
            # 复制表数据
            cursor.execute("insert into server_config_dns_info_backup_20240418 select * from server_config_dns_info;")

        backup_ready_sql2 = "select 1 from information_schema.tables where table_name='server_config_dns_title_backup_20240418' and TABLE_SCHEMA=%s;"
        cursor.execute(backup_ready_sql2, [database])
        res2 = cursor.fetchone()
        if res2:
            print("备份表server_config_dns_title已存在，不再进行备份..")
        else:
            # 复制表结构
            cursor.execute("create table server_config_dns_title_backup_20240418 like server_config_dns_title;")
            # 复制表数据
            cursor.execute("insert into server_config_dns_title_backup_20240418 select * from server_config_dns_title;")
    conn.commit()
    print("备份完成")


if __name__ == '__main__':
    # 0.回滚表
    # reset_2_tables()
    # 1.备份表
    backup_2_tables()


