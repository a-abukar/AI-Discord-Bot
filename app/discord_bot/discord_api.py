from dotenv import load_dotenv
import discord
import os
from app.chatgpt_ai.openai import chatgpt_response
from app.chatgpt_ai.summarize import summarize_messages


load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print("Successfully logged in as: ", self.user)

    async def on_message(self, message):
        print(message.content)
        if message.author == self.user:
            return
        command, user_message=None, None
    
        for text in ['/ai','/bot','/chatgpt']:
            if message.content.startswith(text):
                command=message.content.split(' ')[0]
                user_message=message.content.replace(text, '')
                print(command, user_message)
        
        if command == '/ai' or command == '/bot' or command == '/chatgpt':
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(f"Answer: ```{bot_response}```")

        if message.content.startswith('!summarise'):
            try:
                n = int(message.content.split(' ')[1])
                summary = await summarize_messages(message, n)
                await message.channel.send(f"Summary: ```{summary}```")
            except (ValueError, IndexError):
                await message.channel.send("Please provide a valid number of messages to summarize. Example: !summarise 10")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)