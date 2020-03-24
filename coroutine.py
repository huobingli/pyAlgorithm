import asyncio


async def display(num):
    await asyncio.sleep(1) #
    print(num)

if __name__ == "__main__":
    coroutines = [display(num) for num in range(10)]

    # 获取事件循环并将协程对象放入事件循环中
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(coroutines))
    loop.close()