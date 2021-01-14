# 切片 变量[头下标:尾下标:步长]
str1 = "Hello Worlds!"
print(str1[::-1])

# 字符串格式化
print("我叫 %s 今年 %d 岁!" % ('小明', 10))
# %s 格式化字符串
# %d 格式化整数
# %f 格式化浮点数字，可指定小数点后的精度（四舍五入）
print("保留小数点后3位 %.3f" % 3.1415926)

# str.format
print("我叫 {} 今年 {} 岁!".format('小明', 10))
print("我叫 {1} 今年 {0} 岁!".format('小明', 10))
print("我叫 {0} 今年 {1} 岁! 我叫 {0}".format('小明', 10))

# 三引号 可以包含换行符、制表符以及其他特殊字符,适合处理html或sql
str2 = """<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
"""
print(str2)

# f符号 结果为str类型
print(f"{1+2}")  # 直接计算
# 替换变量
w = {'name': 'Bob', 'age': '22'}
print(f'{w["name"]}: {w["age"]}')

# 常见方法
str3 = "hello woRLd"
print(str3.capitalize())  # 首字母大写，其它改小写
print(str3.title())  # 每个单词首字母改大写
print(str3.upper())  # 全部改大写
print(str3.lower())  # 全部改小写

print(str3.center(20, "*"))  # 以str3为中间位置，两侧填充*至20位
print(str3.count("l", 0, 10))  # 统计l字母出现的次数
print(str3.endswith("Ld"))  # 判断是否以某个字符串结尾
print(str3.startswith("he"))  # 判断是否以某个字符串开始
print(str3.find("llo"))
print(str3.replace("l", "x"))
# print(str3.index())
# print(str3.
