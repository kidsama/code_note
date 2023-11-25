import requests
import concurrent.futures

# 定义要发送的请求的 URL 列表
urls = [
    'http://www.example.com',
    'http://www.example.org',
    'http://www.example.net'
]

# 定义一个函数，用于发送请求并处理响应
def process_url(url):
    response = requests.get(url)
    # 在这里进行响应的处理，可以根据需要自定义逻辑
    return response.text

# 创建一个线程池对象
with concurrent.futures.ThreadPoolExecutor() as executor:
    # 提交每个请求任务到线程池
    futures = [executor.submit(process_url, url) for url in urls]

    # 处理返回的结果
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        # 在这里处理返回结果，可以根据需要自定义逻辑