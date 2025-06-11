import asyncio

async def Hello_World(word):
    await asyncio.sleep(1)
    print(word)

asyncio.run(Hello_World("Hello World"))
