
X = 10000
for i in range(X):
    for j in range(X):
        k = j * i
    print('进度', f'|{"█"*((i+1)*50//X):50}|', f'{(i+1)*100//X}%', end='\r')
print('\n完成！')