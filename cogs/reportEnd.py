from ast import Delete
import asyncio
import discord, os
from discord.ext import commands
from discord import Color, Interaction, ui
from ColorClass import Colors

class reportEnd(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @discord.app_commands.command(name="문의종료", description="문의를 종료합니다")
    async def reportEnd_command(self, interaction: Interaction):
        if interaction.user.guild_permissions.administrator:
            if interaction.channel.category_id == 1247872882701242378:
                reportEmbed = discord.Embed(title="문의종료", description="　", color=Colors.GREEN)
                reportEmbed.add_field(name='　', value='문의가 종료되었습니다.')
                await interaction.channel.send(embed=reportEmbed)
                await asyncio.sleep(5)
                await interaction.channel.delete()
            else:
                errorEmbed = discord.Embed(title='Error', description='　', color=Colors.RED)
                errorEmbed.add_field(name='　', value='이 채널에선 사용할 수 없습니다.')
                await interaction.response.send_message(embed=errorEmbed, ephemeral=True)
        else:
            errorEmbed = discord.Embed(title='Error', description='　', color=Colors.RED)
            errorEmbed.add_field(name='　', value='권한이 없습니다.')
            await interaction.response.send_message(embed=errorEmbed, ephemeral=True)

                

async def setup(client: commands.Bot):
    await client.add_cog(reportEnd(client))