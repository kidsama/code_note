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
print("我叫 {name} 今年 {age} 岁! 我叫 {name}".format_map({"name": "小明", "age": 10}))

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
# 改变大小写系列
print(str3.capitalize())  # 首字母大写，其它改小写
print(str3.title())  # 每个单词首字母改大写
print(str3.upper())  # 全部改大写
print(str3.lower())  # 全部改小写（只包含ASCII字符）
print(str3.casefold())  # 全部改小写（比lower更强大，支持很多不同种类的语言）
print(str3.swapcase())  # 大写改小写，小写改大写

# 判断系列
print(str3.islower())  # 是否全是小写字母
print(str3.isupper())  # 是否全是大写字母
print(str3.istitle())  # 是否每个单词都是首字母大写
print(str3.isdigit())  # 是否是纯数字  PS: Unicode数字，全角数字（双字节），byte数字（单字节）
print(str3.isdecimal())  # 是否是纯数字  PS: Unicode数字，全角数字（双字节）
print(str3.isnumeric())  # 是否是纯数字  PS: Unicode数字，全角数字（双字节），罗马数字，汉字数字
print(str3.isalpha())  # 是否是纯字母
print(str3.isalnum())  # 是否只包含字母或者数字
print(str3.isspace())  # 是否只包含空格
print(str3.isascii())  # 是否都是有效的ASCII字符
print(str3.isprintable())  # 是否都是可打印的字符  PS: 不可打印的字符包括回车符 换行符等 "分割符"的字符
print(str3.isidentifier())  # 是否是有效的Python标识符  PS: 只能有数字字母下划线，不能以数字开头
print(str3.startswith("he", 0, 7))  # 判断在所选区间是否以某个字符串开始
print(str3.endswith("Ld", 0, 7))  # 判断在所选区间是否以某个字符串结尾

# 拼接拆分系列
print(str3.ljust(15, "#"))  # 字符左对齐，在右侧填充#至15位，不传默认空格
print(str3.rjust(15, "#"))  # 字符右对齐，在左侧填充#至15位，不传默认空格
print(str3.center(15, "#"))  # 字符居中，两侧填充#至15位，不传默认空格
print(str3.zfill(15))  # 字符右对齐，在左侧填充0至15位
print(str3.join(["1", "2", "3"]))  # 处理字符串序列，用字符隔开
print(str3.split(" ", 1))  # 通过指定分隔符对字符串进行切片N次，返回列表（从左开始）
print(str3.split(" ", 1))  # 通过指定分隔符对字符串进行切片N次，返回列表（从右开始）
print(str3.splitlines())  # 将字符串按照行('\r', '\r\n', \n')分隔，返回列表
print(str3.partition("l"))  # 如果字符串包含分隔符，则返回一个3元元组，分别为 分隔符左边的子串，分隔符本身，分隔符右边的子串。(从左开始)
print(str3.rpartition("l"))  # 如果字符串包含分隔符，则返回一个3元元组，分别为 分隔符左边的子串，分隔符本身，分隔符右边的子串。(从右开始)

# 计数系列
print(str3.count("ll", 0, 10))  # 统计元素在所选区间出现的次数

# 搜索替换系列
print(str3.find("wo", 0, 10))  # 返回元素在所选区间首次出现的索引值，若没有则返回-1
print(str3.index("wo", 0, 10))  # 返回元素在所选区间首次出现的索引值，若没有则抛出异常
print(str3.rfind("l", 0, 10))  # 返回元素在所选区间最后一次出现的索引值，若没有则返回-1
print(str3.rindex("w", 0, 10))  # 返回元素在所选区间最后一次出现的索引值，若没有则抛出异常
print(str3.strip(" "))  # 移除字符串头尾的指定字符，不传默认为空格
print(str3.lstrip("h"))  # 移除字符串头部的指定字符，不传默认为空格
print(str3.rstrip(" "))  # 移除字符串尾部的指定字符，不传默认为空格
print(str3.replace("l", "#", 2))  # 替换元字符串中的l为# ，最多2次
print(str3.expandtabs())  # 将字符串中的tab符号\t转成N个空格，不传默认为8

# 编码解码
str4 = "我是汉字"
print(str4.encode(encoding="utf-8"))  # 将 str 类型转换成 bytes 类型，这个过程也称为“编码”。
print(str4.encode(encoding="GBK"))

byte_str1 = str4.encode(encoding="utf-8")
print(byte_str1.decode())
byte_str2 = str4.encode(encoding="GBK")
print(byte_str2.decode("GBK"))

# 映射
table = str.maketrans("aeiou", "12345")  # 替换的字典
print(table)
new_str = str3.translate(table)  # 替换完成的字符串
print(new_str)

