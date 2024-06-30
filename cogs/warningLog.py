import asyncio
import discord
from discord.ext import commands
from discord import Interaction, ui
from ColorClass import Colors

class WarningLog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @discord.app_commands.command(name="경고작성", description="경고로그를 작성합니다.")
    async def warning_log(self, interaction: Interaction):
        if interaction.user.guild_permissions.administrator:
            class WarningCreate(ui.Modal, title="경고로그 작성"):
                userID = ui.TextInput(
                    label="경고를 작성할 유저의 ID를 적어주세요.",
                    style=discord.TextStyle.short,
                    placeholder="",
                    required=True
                )
                Reason = ui.TextInput(
                    label="사유와 처벌내용을 적어주세요.",
                    style=discord.TextStyle.long,
                    placeholder="사유 / 처벌",
                    required=True
                )

                async def on_submit(self, interaction: Interaction):
                    user_id = int(self.userID.value)
                    user = interaction.guild.get_member(user_id)
                    
                    if user is None:
                        await interaction.response.send_message("유효한 사용자 ID를 입력하세요.", ephemeral=True)
                        return

                    logEmbed = discord.Embed(title="처벌내역", description='　', color=Colors.GREEN)
                    logEmbed.add_field(name="ID", value=f'{self.userID.value}', inline=False)
                    logEmbed.add_field(name='Name', value=f'{user.name}', inline=False)
                    logEmbed.add_field(name='Reason', value=f'{self.Reason.value}', inline=False)
                    logEmbed.add_field(name='처리자', value=f'@{interaction.user.global_name}', inline=False)
                    
                    channel = interaction.guild.get_channel(1236954778609651813)
                    if channel:
                        await channel.send(embed=logEmbed)
                        await interaction.response.send_message("경고 로그가 성공적으로 작성되었습니다.", ephemeral=True)
                    else:
                        await interaction.response.send_message("유효한 채널 ID를 입력하세요.", ephemeral=True)

            await interaction.response.send_modal(WarningCreate())
        else:
            await interaction.response.send_message("권한이 없습니다.", ephemeral=True)

async def setup(client: commands.Bot):
    await client.add_cog(WarningLog(client))
