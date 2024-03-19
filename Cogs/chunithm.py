import discord
import requests
import json
import load_json_variable as variable

from discord.ext import commands
from discord.ui import Button, View
from bs4 import BeautifulSoup

AIME_URL = 'https://lng-tgk-aime-gw.am-all.net'
LOGIN_URL = 'https://lng-tgk-aime-gw.am-all.net/common_auth/login?site_id=chuniex&redirect_url=https://chunithm-net-eng.com/mobile/&back_url=https://chunithm.sega.com/'
LOGIN_FETCH_URL = 'https://lng-tgk-aime-gw.am-all.net/common_auth/login/sid/'
LOGIN_HEADERS = {
    'Host': AIME_URL.replace('https://', ''),
    'Origin': AIME_URL,
    'Referer': LOGIN_URL
}
LOGIN_PARAMS = {
    'retention': 1,
    'sid': variable.get_parameter('chunithm-bot-sega-id'),
    'password': variable.get_parameter('chunithm-bot-sega-pw')
}

class ChunithmView(View):
    def __init__(self, ctx: commands.Context, friend_code: str):
        super().__init__()
        self.ctx = ctx
        self.friend_code = friend_code
    
    def isExistFriend(friend_code: str) -> bool:
        with requests.Session() as session:
            session.get(LOGIN_URL)
            login_response = session.post(url=LOGIN_FETCH_URL, headers=LOGIN_HEADERS, params=LOGIN_PARAMS, allow_redirects=False)
            session.get(login_response.headers['Location'])

            friend = session.get('https://chunithm-net-eng.com/mobile/friend/')
            friend_soup = BeautifulSoup(friend.text, 'html.parser')
            friend_block = friend_soup.find('input', { 'value': friend_code })
            
            return bool(friend_block)

    @discord.ui.button(label='✔', style=discord.ButtonStyle.success)
    async def button_callback(self, button: Button, interaction: discord.Interaction):
        if interaction.user != self.ctx.author:
            return
    
        if self.isExistFriend(self.friend_code):
            with open('./user/chunithm_user_data.json', 'r') as f:
                user_data = json.load(f)

            user_data[interaction.user.id] = self.friend_code

            with open('./user/chunithm_user_data.json', 'w') as f:
                json.dump(user_data, f, indent=4)

            await interaction.channel.send(
                embed=discord.Embed(
                    title='✔ 등록이 완료되었습니다.',
                    color=discord.Color.from_str('#00FF00')
                )
            )

        else:
            await interaction.channel.send(
                embed=discord.Embed(
                    title='❌ 등록에 실패했습니다.',
                    color=discord.Color.from_str('#FF0000')
                )
            )
            
        

class Chunithm(commands.Cog):
    def __init__(self, app: commands.Bot):
        self.app = app

    @commands.command()
    async def chunithm(self, ctx: commands.Context):
        await ctx.send("chunithm 명령어 테스트")

    @commands.command()
    async def register(self, ctx: commands.Context, friend_code: str):
        with open('./user/chunithm_user_data.json', 'r') as f:
            user_data = json.load(f)

        if not friend_code or not friend_code.isnumeric():
            await ctx.send('올바르지 않은 친구 코드 형식입니다.')
            return

        if ctx.author.id in user_data:
            await ctx.send('이미 등록된 유저입니다.')
            return
                    
        with requests.Session() as session:
            session.get(LOGIN_URL)
            login_response = session.post(
                url=LOGIN_FETCH_URL, 
                headers=LOGIN_HEADERS, 
                params=LOGIN_PARAMS, 
                allow_redirects=False
            )
            AUTH_TOKEN = session.get(login_response.headers['Location']).cookies['_t']
            send_invite = session.post('https://chunithm-net-eng.com/mobile/friend/search/sendInvite/', data={
                'idx': friend_code,
                'token': AUTH_TOKEN
            })

        if send_invite.status_code == 200:
            embed = discord.Embed(
                title='친구 요청을 전송하였습니다.',
                description='받은 담에 아래 버튼 처 누르세요',
                color=discord.Color.from_str('#00FF00')
            )
            await ctx.send(embed=embed, view=ChunithmView(ctx, friend_code))
        else:
            await ctx.send(f'친구 요청 전송에 실패하였습니다. Error Code: {send_invite.status_code}')

async def setup(app: commands.Bot):
    await app.add_cog(Chunithm(app))
