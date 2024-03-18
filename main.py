import asyncio
import os.path

import discord
from discord.ext import commands

import load_json_variable as variable

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents, sync_command=True,)
cogs_path = 'Cogs'
abs_cogs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), cogs_path)


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


async def unload_extensions(extension=None):
    if extension is not None:
        try:
            await bot.unload_extension(f"Cogs.{extension}")
        except (commands.ExtensionNotLoaded, commands.ExtensionNotFound):
            pass
    else:
        for filename in os.listdir("Cogs"):
            if filename.endswith('.py'):
                try:
                    await bot.unload_extension(f"Cogs.{filename[:-3]}")
                except (commands.ExtensionNotLoaded, commands.ExtensionNotFound):
                    pass


async def load_extensions():
    for filename in os.listdir(abs_cogs_path):
        if filename.endswith('.py'):
            await bot.load_extension(f'Cogs.{filename[:-3]}')


@bot.command(name='reload')
async def reload_extensions(ctx, extension=None):
    if extension is not None:
        await unload_extensions(extension)
        try:
            await bot.load_extension(f"Cogs.{extension}")
        except commands.ExtensionNotFound:
            await ctx.send(f"'{extension}' 파일을 찾을 수 없습니다.")
        except (commands.NoEntryPointError, commands.ExtensionFailed) as e:
            await ctx.send(f"'{extension}' 을(를) 불러오는 도중 에러가 발생했습니다.\n{e}")
        else:
            await ctx.send(":white_check_mark:")
    else:
        for filename in os.listdir(abs_cogs_path):
            if filename.endswith('.py'):
                await unload_extensions(filename[:-3])
                try:
                    await bot.load_extension(f"Cogs.{filename[:-3]}")
                except commands.ExtensionNotFound:
                    await ctx.send(f"'{filename[:-3]}' 파일을 찾을 수 없습니다.")
                except (commands.NoEntryPointError, commands.ExtensionFailed) as e:
                    await ctx.send(f"'{filename[:-3]}' 을(를) 불러오는 도중 에러가 발생했습니다.\n{e}")

        await ctx.send(":white_check_mark:")


async def main():
    async with bot:
        await load_extensions()
        await bot.start(variable.get_token())


asyncio.run(main())
