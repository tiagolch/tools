from pyrogram import Client
from decouple import config

app = Client(
    "extractawb_bot"
    # ,
    # api_id=config('API_ID_BOT'),
    # api_hash=config('API_HASH_BOT'),
    # bot_token=config('TOKEN_BOT')
)

async def main():
    async with app:
        # Get information about the bot itself
        me = await app.get_me()

        # Check if the bot is not sending a message to itself
        if me.username != "extractawb_bot":
            await app.send_message("me", "Hi!")

if __name__ == "__main__":
    app.run(main())
