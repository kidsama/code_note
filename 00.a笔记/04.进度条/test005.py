from alive_progress import alive_bar

X = 10000
with alive_bar(X) as bar:
    for i in range(X):
        for j in range(X):
            k = j * i
        bar()
print('完成！')