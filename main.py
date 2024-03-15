import asyncio
import os.path

import discord
from discord.ext import commands

import load_json_variable as variable

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)


@bot.event
async def on_ready():
    """
    봇이 로딩될 시 실행 되는 event

    :return: None
    """
    await bot.change_presence(
        activity=discord.CustomActivity(name='maimai DX BUDDiES', emoji=discord.PartialEmoji(name='U+2728')))
    print(f"logged in as {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return None

    await bot.process_commands(message)


async def load_extensions():
    cogs_path = 'Cogs'
    abs_cogs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), cogs_path)
    for filename in os.listdir(abs_cogs_path):
        if filename.endswith('.py'):
            await bot.load_extension(f'Cogs.{filename[:-3]}')


async def main():
    async with bot:
        await load_extensions()
        await bot.start(variable.get_token())


asyncio.run(main())
