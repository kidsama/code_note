from progress.bar import Bar
X = 10000
with Bar('进度', max=X) as bar:
    for i in range(X):
        for j in range(X):
            k = j * i
        bar.next()
print('\n完成！')