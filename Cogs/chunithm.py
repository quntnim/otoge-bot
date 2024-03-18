import discord
from discord.ext import commands


class Chunithm(commands.Cog):
    def __init__(self, app):
        self.app = app

    @commands.command()
    async def chunithm(self, ctx):
        await ctx.send(str(type(ctx)))
        await ctx.send("chunithm 명령어 테스트")


async def setup(app):
    await app.add_cog(Chunithm(app))
