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


@bot.command(name="test")
async def test(ctx):
    await ctx.channel.send("Test command executed")


bot.run(variable.get_token())
