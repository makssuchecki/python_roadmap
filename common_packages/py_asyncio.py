import asyncio
# asyncio is a library to write concurrent code using async/await syntax

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World!")

asyncio.run(main())