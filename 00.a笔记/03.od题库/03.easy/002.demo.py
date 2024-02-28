"""
题目描述
输入单行英文句子,里面包含英文字母,空格以及,.?
三种标点符号,请将句子内每个单词进行倒序,并输出倒序后的语句
输入描述
输入字符串 S,S 的长度 1≤N≤100
输出描述
输出逆序后的字符串
"""


def func():
    # sentence_str = input()
    sentence_str = "I am a student.  Do you like Python? I like python."
    sentence_list = sentence_str.split()
    for i in range(len(sentence_list)):
        sentence_list[i] = sentence_list[i][::-1]
        if sentence_list[i] and sentence_list[i][0] in [",", ".", "?"]:
            sentence_list[i] = sentence_list[i][1:] + sentence_list[i][0]

    print(" ".join(sentence_list))


if __name__ == '__main__':
    func()
