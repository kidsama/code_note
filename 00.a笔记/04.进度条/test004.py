
from tqdm import tqdm, trange

X = 10000
# for i in tqdm(range(X)):
for i in trange(X):
    for j in range(X):
        k = j * i
print('完成！')