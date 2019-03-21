import asyncio


async def foo():
    yield from iter(range(10))


async def main():
    async for x in foo():
        print(x * 2)


asyncio.run(main())
