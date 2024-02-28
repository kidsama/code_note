import json


def func1():
    with open("bookmarks-2024-01-18-09-19-14.json", "r") as f:
        data = json.loads(f.read())
        bookmarks = data.get("bookmarks")

        pass_list = []
        for i in bookmarks:
            pass_list.append({
                "host": i.get("host"),
                "username": i.get("username"),
                "password": i.get("password")

            })
        # 根据host排序
        pass_list.sort(key=lambda x: x.get("host"))
        print(json.dumps(pass_list))


if __name__ == '__main__':
    func1()