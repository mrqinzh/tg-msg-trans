from telethon import TelegramClient, events
import asyncio

# 填入你的 API ID、API Hash 和会话名称
api_id = APP_ID
api_hash = 'APP_HASH'
session_name = 'session_name'

client = TelegramClient(session_name, api_id, api_hash)

async def get_channel_ids():
    await client.start()
    async for dialog in client.iter_dialogs():
        if dialog.is_channel:
            print(f'频道名称: {dialog.name}, 频道 ID: {dialog.entity.id}')

    await client.disconnect()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_channel_ids())
