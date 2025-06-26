import asyncio

async def Hello_World(word):
    await asyncio.sleep(1)
    print(word)

asyncio.run(Hello_World("Hello World"))

async def main():
    await asyncio.gather(
        Hello_World("Hello World"),
        Hello_World("Hello World"),
    )

asyncio.run(main())
