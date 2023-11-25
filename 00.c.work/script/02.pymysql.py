import pymysql
import uuid

# 连接数据库
conn = pymysql.connect(host='localhost', user='root', password='lwx984502', db='kcm_main')

# 创建游标
cursor = conn.cursor()

# # 创建一级组织
# first_uuid = uuid.uuid4().hex
# print(first_uuid)
# sql = f"INSERT INTO `area` VALUES ('{first_uuid}', '6000组织', NULL, '{first_uuid}', '1', 2, 1, 'admin', '2023-11-03 18:27:34', '', 0, 76, ',1,76', NULL, '2023-11-03 18:27:34', NULL, 9999999);"
# cursor.execute(sql)

# # 创建二级组织
# for i in range(77, 6077):
#     this_uuid = uuid.uuid4().hex
#     sql = f"INSERT INTO `area` VALUES ('{this_uuid}', '二级组织{i}', NULL, '{this_uuid}', '{first_uuid}', 2, 1, 'admin', '2023-11-03 18:27:34', '', 0, {i}, ',1,76,{i}', NULL, '2023-11-03 18:27:34', NULL, 9999999);"
#     cursor.execute(sql)


# # 使用executemany()方法执行多个SQL语句
# # cursor.execute(sql)
#
# # # 确认并提交更改
# conn.commit()
#
# # 关闭游标和数据库连接
# cursor.close()
# conn.close()

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


def del_6000(pid):
    with conn.cursor() as cursor:
        sql = f"delete from area where pid='{pid}'"
        cursor.execute(sql)

        cursor.execute(f"delete from area where id='{pid}'")
        cursor.execute(f"delete from area_sum_relationships where software_sum=3345")
    conn.commit()

def create_first():
    # 创建一级组织
    first_uuid = "82a3d50c7b4e4609ae88c9a8fbbbe889"
    print(first_uuid)
    sql = f"INSERT INTO `area` VALUES ('{first_uuid}', '6000组织', NULL, '{first_uuid}', '1', 2, 1, 'admin', '2023-11-03 18:27:34', '', 0, 76, ',1,76', NULL, '2023-11-03 18:27:34', NULL, 9999999);"
    cursor.execute(sql)

    cursor.execute(f"INSERT INTO `area_sum_relationships` VALUES ('{uuid.uuid4().hex}', '{first_uuid}', 6000, 0, 0, 3345);")

    conn.commit()


if __name__ == '__main__':
    # 创建一级组织
    # create_first()
    #
    # # 创建6000二级组织
    create_6000("82a3d50c7b4e4609ae88c9a8fbbbe889")

    # 删除
    # del_6000("82a3d50c7b4e4609ae88c9a8fbbbe889")