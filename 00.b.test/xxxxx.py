def func1():
    try:
        aaa = 1/0
        return "aaa"
    except Exception as e:
        pass

xxx = func1()
print("xxx:", xxx)
