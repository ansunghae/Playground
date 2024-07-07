from ast import Delete
import asyncio
import discord, os
from discord.ext import commands
from discord import Color, Interaction, ui
from ColorClass import Colors

class reportEnd(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @discord.app_commands.command(name="문의종료", description="문의를 종료합니다") #문의 종료하는 슬래쉬 커맨드및 그에 대한 커맨드 설명
    async def reportEnd_command(self, interaction: Interaction): #
        if interaction.user.guild_permissions.administrator: #만약에 상호작용한 유저가 서버의 관리자라면
            if interaction.channel.category_id == 1247872882701242378: #만악에 상호작용한 채널의 아이디가 ~라면
                reportEmbed = discord.Embed(title="문의종료", description="　", color=Colors.GREEN) #초록색의 임베드 제목은 문의종료 상세 정보는 공백
                reportEmbed.add_field(name='　', value='문의가 종료되었습니다.') #상세정보 문의가 종료되었습니다.추가
                await interaction.channel.send(embed=reportEmbed) #임베드 발송
                await asyncio.sleep(5) #5초 대기
                await interaction.channel.delete() #삭제
            else: #상호작용한 서버의 아이디가 다를때
                errorEmbed = discord.Embed(title='Error', description='　', color=Colors.RED) #빨간색의 임베드 제목은 에러 상세정보는 공백
                errorEmbed.add_field(name='　', value='이 채널에선 사용할 수 없습니다.') #상세정보 이 채널에서는 사용 할수 없습니다. 추가
                await interaction.response.send_message(embed=errorEmbed, ephemeral=True) #임베드 발송
        else: #서버 관리자 권한이 없을때
            errorEmbed = discord.Embed(title='Error', description='　', color=Colors.RED) #빨간색의 임베드 제목은 에러 상세정보는 공백
            errorEmbed.add_field(name='　', value='권한이 없습니다.') #상세정보 이 채널에서는 사용 할수 없습니다. 추가
            await interaction.response.send_message(embed=errorEmbed, ephemeral=True) #임베드 발송

                

async def setup(client: commands.Bot):
    await client.add_cog(reportEnd(client))