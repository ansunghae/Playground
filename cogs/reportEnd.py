from ast import Delete
import asyncio
import discord, os
from discord.ext import commands
from discord import Interaction, ui

class reportEnd(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @discord.app_commands.command(name="문의종료", description="문의를 종료합니다")
    async def reportEnd_command(self, interaction: Interaction):
        if interaction.user.guild_permissions.administrator:
            if interaction.channel.category_id == 1247872882701242378:
                reportEmbed = discord.Embed(title="문의종료", description="　")
                reportEmbed.add_field(name='　', value='문의가 종료되었습니다.')
                await interaction.channel.send(embed=reportEmbed)
                await asyncio.sleep(5)
                await interaction.channel.delete()
            else:
                await interaction.response.send_message("아니 등신아 그걸 왜 여기서 쳐 씀?", ephemeral=True)
        else:
            await interaction.response.send_message("권한이 없습니다.", ephemeral=True)

                

async def setup(client: commands.Bot):
    await client.add_cog(reportEnd(client))