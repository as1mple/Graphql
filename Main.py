import asyncio
import time

from logic import run
from setting import input_args, condition

if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run((input_args())))
    loop.run_until_complete(future)
    print('Work time took : ', time.time() - start)
