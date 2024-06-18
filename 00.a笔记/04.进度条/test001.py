
X = 10000
for i in range(X):
    for j in range(X):
        k = j * i
    print(f'{i+1} / {X}', end='\r')
print('\n完成！')