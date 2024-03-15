import discord
from discord.ext import commands


class Maimai(commands.Cog):
    def __init__(self, app):
        self.app = app

    @commands.command()
    async def maimai(self, ctx):
        await ctx.send("maimai 명령어 테스트")


async def setup(app):
    await app.add_cog(Maimai(app))
