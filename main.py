import asyncio
import os

from bohe_sign.login import get_bohe_token


async def main():
    bohe_token, linux_do_connect_token, linux_do_token = await get_bohe_token()

    if bohe_token:
        print("Successfully obtained Bohe Token")
    else:
        print("Failed to obtain Bohe Token")


if __name__ == "__main__":
    asyncio.run(main())