from app.chatgpt_ai.openai import chatgpt_response
import asyncio

async def summarize_messages(message, n, min_length=50):
    messages_to_summarize = []
    async for msg in message.channel.history(limit=n, before=message):
        author_display_name = msg.author.display_name
        messages_to_summarize.append(f"{author_display_name}: {msg.content}")
    messages_text = ' '.join(messages_to_summarize)

    # Check if the length of the messages is above the minimum threshold
    if len(messages_text) > min_length:
        summary = chatgpt_response(f"Please summarize the following text in bullet point fashion, mentioning usernames in your summary in speech marks but not repetitively: {messages_text}")
    else:
        summary = "There is not enough information to generate a summary. Please provide more context."

    return summary


