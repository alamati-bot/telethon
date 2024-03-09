from telethon import TelegramClient, events, types

print("iuhduia")

api_id = '29781864'
# api_hash = os.environ['hash']
api_hash = 'cc05cf284195557866937e39bdb91cd7'
phone_number = '+963994232087'
channel_username = '@yyffghgguhfyjgyjhfghff6hg'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

@client.on(events.NewMessage(chats=channel_username))
async def my_event_handler(event):
    print(f"New Message: {event.text}")
    if event.media:
        if event.media.document:
            for attr in event.media.document.attributes:
                if isinstance(attr, types.DocumentAttributeFilename):
                    if attr.file_name.endswith('.zip'):
                        zip_path = await client.download_media(message=event.message)
                        await unzip_and_process(zip_path)

async def unzip_and_process(zip_path):
    print("working")


print("jjkk")
client.run_until_disconnected()
