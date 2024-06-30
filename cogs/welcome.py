import discord
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.member):
        guild = member.guild

        DmMessage = discord.Embed(title="환영합니다", description='　', color=0x00ff00)
        DmMessage.add_field(name='　',value=f'{member.mention}님! 놀이터서버에 오신것을 환영합니다!\n규칙을 잘 읽고 인증하신 후 즐겁게 활동해주세요!')
        DmMessage.add_field(name='　',value=f'<#972334185677221898> 에서 자기소개를 통해 서버의 모든것을 즐겨보세요!')

        SvMessage = discord.Embed(title="👋 환영합니다", description='　', color=0x00ff00)
        SvMessage.add_field(name='　',value="새로운분이 서버에 가입했어요!")
        SvMessage.set_footer(text="다들 뉴하를 외쳐주세요!")
        channel = guild.get_channel(986193415035314207)

        ChMessage = discord.Embed(title=f'{member.display_name}님이 서버에 들어왔어요!', description='모두들 뉴하를 외쳐주세요!', color=0x00ff00)
        channelChat = guild.get_channel(1236950487262040144)
        
        try:
            await member.send(embed = DmMessage)
        except:
            pass

        await channelChat.send(f'<@&963749174053052456>여러분! 새로운 유저가 들어왔어요!', embed=ChMessage)
        await channel.send(f'{member.mention}님! 환영합니다!', embed=SvMessage)
        print(f'{member}님이 들어왔습니다.')

async def setup(bot):
    await bot.add_cog(Welcome(bot))
