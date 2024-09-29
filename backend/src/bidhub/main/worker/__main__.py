import asyncio

from .app import create_worker


if __name__ == '__main__':
    app = create_worker()
    asyncio.run(app.run())
