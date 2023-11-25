import pymysql
import uuid

# 连接数据库
conn = pymysql.connect(host='localhost', user='root', password='lwx984502', db='kcm_main')

# 创建游标
cursor = conn.cursor()

def create_6000(pid):
    with conn.cursor() as cursor:
        for i in range(8077, 10077):
            this_uuid = uuid.uuid4().hex
            sql = f"INSERT INTO `area` VALUES ('{this_uuid}', '二级组织{i}', NULL, '{this_uuid}', '{pid}', 2, 1, 'admin', '2023-11-03 18:27:34', '', 0, {i}, ',1,76,{i}', NULL, '2023-11-03 18:27:34', NULL, 9999999);"
            # print(sql)
            cursor.execute(sql)
            cursor.execute(
                f"INSERT INTO `area_sum_relationships` VALUES ('{uuid.uuid4().hex}', '{this_uuid}', 0, 0, 0, 3345);")
    conn.commit()


if __name__ == '__main__':
    # 创建一级组织
    # create_6000("82a3d50c7b4e4609ae88c9a8fbbbe889")
    pass
    # 删除
    # del_6000("82a3d50c7b4e4609ae88c9a8fbbbe889")

    # 备份表结构


    # 备份表数据

    # 还原表结构