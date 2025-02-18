from telethon import TelegramClient, events
import asyncio

# 填入你从 Telegram 官网获取的 API ID 和 API Hash
api_id = YOUR_APP_ID
api_hash = 'YOUR_APP_HASH'

# 你可以自定义会话名称，这里使用 'session_name'
session_name = 'session_name'

proxy = ('http', '127.0.0.1', 7890)

# 创建 Telegram 客户端实例
client = TelegramClient(session_name, api_id, api_hash, proxy=proxy)

# 填入要监听的频道 ID 和要转发到的频道 ID
source_channel_ids = [243235581339]
destination_channel_id = 236144947472


# 定义一个异步函数来处理接收到的新消息事件
@client.on(events.NewMessage(chats=source_channel_ids))
async def handle_new_message(event):
    message = event.message
    try:
        # 将消息转发到目标频道
        await client.forward_messages(destination_channel_id, message)
        print(f'已将消息转发到目标频道：{message.text}')
    except Exception as e:
        print(f'转发消息时出现错误：{e}')


# 定义主异步函数
async def main():
    # 启动客户端
    await client.start()
    print('已成功连接到 Telegram')
    # 让客户端持续运行，直到手动停止
    await client.run_until_disconnected()


if __name__ == '__main__':
    # 运行主异步函数
    asyncio.run(main())

# requirements.txt 
# telethon
# pysocks
