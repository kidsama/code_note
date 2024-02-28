import re
import json
import pymysql

# 连接 MySQL 数据库
conn = pymysql.connect(
    host='127.0.0.1',  # 主机名
    port=3306,         # 端口号，MySQL默认为3306
    user='root',       # 用户名
    password='lwx984502',  # 密码
    database='liu',   # 数据库名称
)


def in_check():
    with conn.cursor() as cursor:
        with open("1.txt", "r") as f:
            files = f.readlines()

            for i in files:
                line = i.strip()
                if line:
                    line_without_blank = line.replace(" ", "")
                    line_spilt = line_without_blank.split(".")
                    content = line_spilt[1].replace("（错）", "").replace("（对）", "")
                    options = {"A": "对", "B": "错"}
                    if line_spilt[1].endswith("（错）"):
                        answer = "B"
                    elif line_spilt[1].endswith("（对）"):
                        answer = "A"
                    else:
                        answer = "题库格式不规范，没解析出来答案"
                    sql = f"insert into l_tiku (content, options, answer, type) values ('{content}', '{json.dumps(options, ensure_ascii=False)}', '{answer}', 1);"
                    cursor.execute(sql)
            conn.commit()


def in_chance():
    with conn.cursor() as cursor:
        with open("2.txt", "r") as f:
            file_content = f.read()
            question_list = file_content.split("\n\n")
            for one_test in question_list[:]:  # 遍历所有题目
                if one_test.strip():
                    end_test = ""  # 题干
                    options = {}
                    for item in one_test.strip().split("\n"):
                        if item.lstrip()[0].isdigit():  # 是题目
                            end_test = end_test + item
                        elif item.lstrip() and item.lstrip()[0] == "A":
                            options["A"] = item.lstrip()[1:]
                        elif item.lstrip() and item.lstrip()[0] == "B":
                            options["B"] = item.lstrip()[1:]
                        elif item.lstrip() and item.lstrip()[0] == "C":
                            options["C"] = item.lstrip()[1:]
                        elif item.lstrip() and item.lstrip()[0] == "D":
                            options["D"] = item.lstrip()[1:]
                        elif item.lstrip() and item.lstrip()[0] == "E":
                            options["E"] = item.lstrip()[1:]
                        elif item.lstrip() and item.lstrip()[0] == "F":
                            options["F"] = item.lstrip()[1:]
                        else:
                            end_test = end_test + item

                    main_content_list = end_test.split(".")[1:]
                    main_content = ""
                    for i in main_content_list:
                        main_content = main_content + i
                    # 找出答案
                    main_content_without_blank = main_content.strip().replace(" ", "")
                    answer_list = re.findall(r"[（]([A-F]*?)[）]", main_content_without_blank)
                    if len(answer_list) == 0:
                        answer = "题库格式不规范，没解析出来答案"
                        print("===", answer_list, main_content_without_blank)
                        l_type = 2  # 单选
                    else:
                        answer = answer_list[0]
                        if len(answer) == 1:
                            l_type = 2
                        else:
                            l_type = 3  # 多选
                    # 生成题目
                    end_content = main_content_without_blank.replace(answer, "")
                    sql = "insert into l_tiku (content, options, answer, type) values ('{}','{}','{}', {});".format(
                        end_content, json.dumps(options, ensure_ascii=False), answer, l_type
                    )
                    cursor.execute(sql)
            conn.commit()

def clear_data():
    with conn.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE l_tiku")
        conn.commit()
        print("清理完毕")

def make_demo():
    with conn.cursor() as cursor:
        cursor.execute("select * from l_tiku")
        questions_arry = []
        choose_arry = []
        answer_arry = []


        for item in cursor.fetchall():
            questions_arry.append(item[1])
            choose_item = json.loads(item[2])
            this_all_choose = []
            for temp in choose_item.keys():
                this_all_choose.append(f"{temp}.{choose_item[temp]}")
            choose_arry.append(this_all_choose)
            answer_arry.append(item[3])
        print("questionsArry: ", questions_arry, ",")
        print("chooseArry: ", choose_arry, ",")
        print("answerArry:", answer_arry)


if __name__ == '__main__':
    # clear_data()
    in_check()
    in_chance()

    # make_demo()

