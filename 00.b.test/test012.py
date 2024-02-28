# from pathvalidate import is_valid_filename
# filename = "....my_file"
#
# if is_valid_filename(filename):
#     print("文件名合法")
# else:
#     print("文件名不合法")
#
# import re
#
# def check_file_name(fileName: str) -> bool:
#     p = "[^\\s\\\\/:\\*\\?\\\"<>\\|](\\x20|[^\\s\\\\/:\\*\\?\\\"<>\\|])*[^\\s\\\\/:\\*\\?\\\"<>\\|\\.]$"
#     if not re.match(p, fileName):
#         return False
#     return True
#
#
# print(check_file_name("123.txt"))
# print(check_file_name(".txt"))
# print(check_file_name("../a.log"))
# print(check_file_name(".txt."))
# print(check_file_name(".txt."))

def check_file_name(file_name):
    if "/" in file_name:
        return False
    return True

