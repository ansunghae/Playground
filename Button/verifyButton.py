import discord
from discord import Guild, Intents, Game, Status, Object, ButtonStyle, app_commands, ui, Interaction, Message, User, PartialEmoji, SelectOption, CategoryChannel, PermissionOverwrite, permissions
from discord.ui import Button, View, Select, Modal, TextInput
from discord.ext import commands
from discord.utils import get

class verify_button(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="자기소개 작성하기", style=discord.ButtonStyle.green, custom_id="verify_button")
    async def report_Btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        class verifyModal(ui.Modal, title="자기소개 작성하기"):
                    name = ui.TextInput(
                        label="닉네임을 입력해주세요.",
                        style=discord.TextStyle.short,
                        placeholder="닉네임은 본인의 닉네임으로 설정됩니다.",
                        required=True
                    )
                    selfinfo = ui.TextInput(
                        label="간단하게 자기소개를 해주세요",
                        style=discord.TextStyle.long,
                        placeholder="",
                        required=True
                    )
                    age = ui.TextInput(
                          label="본인의 나이를 입력해주세요.",
                          style=discord.TextStyle.short,
                          placeholder="나이는 운영팀만 확인하며, 통계를 위해 집계합니다.",
                          required=True
                    )
                    async def on_submit(self, interaction: Interaction):
                        selfEmbed = discord.Embed(title=f'{self.name.value}님이 자기소개를 작성하셨어요!')
                        selfEmbed.add_field(name="　", value=f'{self.selfinfo.value}')

                        logEmbed = discord.Embed(title="자기소개 작성로그")
                        logEmbed.add_field(name='　', value=f'{interaction.user.mention}님이 자기소개를 작성하셨습니다.', inline=False)
                        logEmbed.add_field(name='내용', value=f'{self.selfinfo.value}', inline=False)
                        logEmbed.add_field(name='나이', value=f'{self.age.value}', inline=False)


                        await interaction.user.edit(nick=f'{self.name.value}')
                        await interaction.user.add_roles(interaction.guild.get_role(963749174053052456)) # 유저역할 지급
                        await interaction.user.remove_roles(interaction.guild.get_role(1248592343376859166)) # 뉴비역할 제거
                        await interaction.guild.get_channel(1236950487262040144).send(embed=selfEmbed) # 자유채팅에 전송
                        await interaction.guild.get_channel(986194109318438962).send(embed=logEmbed)
                        await interaction.response.send_message("자기소개 작성이 완료되었습니다.", ephemeral=True)
        await interaction.response.send_modal(verifyModal())
        