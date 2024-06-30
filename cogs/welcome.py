import discord, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

PublicChannel = os.getenv('PUBLIC_CHANNEL')
WelcomeChannel = os.getenv('WELCOME_CHANNEL')

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.member):
        guild = member.guild

        SvMessage = discord.Embed(title="👋 환영합니다", description='　', color=0x00ff00) # 환영채널 메시지 전송
        SvMessage.add_field(name='　',value="새로운분이 서버에 가입했어요!")
        SvMessage.set_footer(text="다들 뉴하를 외쳐주세요!")
        welcome_Channel = guild.get_channel(WelcomeChannel)

        ChMessage = discord.Embed(title=f'{member.display_name}님이 서버에 들어왔어요!', description='모두들 뉴하를 외쳐주세요!', color=0x00ff00) # 자유채팅 메시지 전송 
        public_Channel = guild.get_channel(PublicChannel)

        await public_Channel.send(f'<@&963749174053052456>여러분! 새로운 유저가 들어왔어요!', embed=ChMessage)
        await welcome_Channel.send(f'{member.mention}님! 환영합니다!', embed=SvMessage)
        print(f'{member}님이 들어왔습니다.')

async def setup(bot):
    await bot.add_cog(Welcome(bot))
