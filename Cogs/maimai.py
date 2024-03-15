import datetime
import json

import discord
from discord.ext import commands


class Maimai(commands.Cog):
    def __init__(self, app):
        self.app = app

    @commands.command()
    async def maimai(self, ctx):
        await ctx.send("maimai 명령어 테스트")

    @commands.command(name='mai-search')
    async def search(self, ctx, arg):
        with open('./data/maimai_data.json', 'r', encoding='UTF-8') as f:
            json_data = json.load(f)
            for k in json_data['songs']:
                if arg.upper() in k['songId'].upper():
                    print(k)

        embed = discord.Embed(
            title="Straight into the lights\n<:dx1:1218056379458261112><:dx2:1218056391982583849><:dx3:1218056405681180813>",
            url="https://www.youtube.com/results?search_query=maimai+Straight+into+the+lights",
            description="> Cosmograph / maimai",
            colour=0x00b0f4,
            timestamp=datetime.datetime.now())

        embed.set_author(name="곡 검색", url="https://example.com")

        embed.add_field(name="BASIC",
                        value="4",
                        inline=False)
        embed.add_field(name="ADVANCED",
                        value="8",
                        inline=False)
        embed.add_field(name="EXPERT",
                        value="12 (12.5)",
                        inline=False)
        embed.add_field(name="MASTER",
                        value="14+ (14.8)",
                        inline=False)
        embed.set_thumbnail(
            url="https://dp4p6x0xfi5o9.cloudfront.net/maimai/img/cover/8fc940a2fcffd56224e372b2a57888e84ca295c43609dad8a185b14227caf2a8.png")

        embed.set_footer(text="otoge-bot")

        await ctx.send(embed=embed)


async def setup(app):
    await app.add_cog(Maimai(app))
