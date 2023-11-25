import asyncio
import aiohttp

# 定义要请求的接口 URL 列表
urls = [
    'http://www.example.com',
    'http://www.example.org',
    'http://www.example.net'
]


# 定义一个异步函数，用于发送请求并处理响应
async def process_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # 在这里进行响应的处理，可以根据需要自定义逻辑
            response_text = await response.text()
            return response_text


# 创建一个事件循环
loop = asyncio.get_event_loop()

# 创建一个任务列表
tasks = [process_url(url) for url in urls]

# 执行任务并获取结果
results = loop.run_until_complete(asyncio.gather(*tasks))

# 处理返回的结果
for result in results:
    # 在这里处理返回结果，可以根据需要自定义逻辑
    print(result)
