import asyncio
import discord
from discord.ext import commands
from discord import Interaction, ui

class AdminVerify(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @discord.app_commands.command(name="강제인증", description="유저를 강제로 인증합니다.")
    async def AdminVerify(self, interaction: Interaction):
        if interaction.user.guild_permissions.administrator:
            class AdminVerify(ui.Modal, title="경고로그 작성"):
                userID = ui.TextInput(
                    label="강제인증을 진행할 유저의 아이디를 입력하세요.",
                    style=discord.TextStyle.short,
                    placeholder="",
                    required=True
                )

                async def on_submit(self, interaction: Interaction):
                    user_id = int(self.userID.value)
                    user = interaction.guild.get_member(user_id)
                    
                    if user is None:
                        await interaction.response.send_message("유효한 사용자 ID를 입력하세요.", ephemeral=True)
                        return

                    selfEmbed = discord.Embed(title=f'{user.global_name}님이 자기소개를 작성하셨어요!')
                    selfEmbed.add_field(name="　", value='관리진 강제인증')
                    
                    channel = interaction.guild.get_channel(1236950487262040144)
                    await channel.send(embed=selfEmbed)
                    await interaction.response.send_message("강제인증이 완료되었습니다.", ephemeral=True)
                    await user.add_roles(interaction.guild.get_role(963749174053052456)) # 유저역할 지급
                    await user.remove_roles(interaction.guild.get_role(1248592343376859166)) # 뉴비역할 제거
            await interaction.response.send_modal(AdminVerify())
        else:
            await interaction.response.send_message("권한이 없습니다.", ephemeral=True)

async def setup(client: commands.Bot):
    await client.add_cog(AdminVerify(client))
