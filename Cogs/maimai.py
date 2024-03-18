import datetime
import json

import discord
import asyncio
from discord.ext import commands


class Maimai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def maimai(self, ctx):
        await ctx.send("maimai 명령어 테스트0")

    @commands.command(name='mai-search')
    async def search(self, ctx, *, arg):
        filtered_data = []
        idx = 0
        search_result = ''
        with open('./data/maimai_data.json', 'r', encoding='UTF-8') as f:
            json_data = json.load(f)
            for temp in json_data['songs']:
                if arg.upper() in temp['songId'].upper():
                    filtered_data.append(temp)
                    search_result += f"{idx} {temp['title']}\n"
                    idx += 1
        await ctx.send(search_result)
        if idx > 2:
            msg = await self.bot.wait_for("message", timeout=30)
            print(msg.content)
            await ctx.send(filtered_data[int(msg.content)])
        else:
            await ctx.send(filtered_data)


        # embed = discord.Embed(
        #     title="Straight into the lights\n<:dx1:1218056379458261112><:dx2:1218056391982583849><:dx3:1218056405681180813>",
        #     url="https://www.youtube.com/results?search_query=maimai+Straight+into+the+lights",
        #     description="> Cosmograph / maimai",
        #     colour=0x00b0f4,
        #     timestamp=datetime.datetime.now())
        #
        # embed.set_author(name="곡 검색", url="https://example.com")
        #
        # embed.add_field(name="BASIC",
        #                 value="4",
        #                 inline=False)
        # embed.add_field(name="ADVANCED",
        #                 value="8",
        #                 inline=False)
        # embed.add_field(name="EXPERT",
        #                 value="12 (12.5)",
        #                 inline=False)
        # embed.add_field(name="MASTER",
        #                 value="14+ (14.8)",
        #                 inline=False)
        # embed.set_thumbnail(
        #     url="https://dp4p6x0xfi5o9.cloudfront.net/maimai/img/cover/8fc940a2fcffd56224e372b2a57888e84ca295c43609dad8a185b14227caf2a8.png")
        #
        # embed.set_footer(text="otoge-bot")
        #
        # await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Maimai(bot))
