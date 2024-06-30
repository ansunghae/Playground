import discord
from discord import Intents, Game, Status, Object, ButtonStyle, app_commands, ui, Interaction, Message, User, PartialEmoji, SelectOption, CategoryChannel, PermissionOverwrite, permissions
from discord.ui import Button, View, Select, Modal, TextInput
from discord.ext import commands
from discord.utils import get

class report_button(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="문의 또는 신고하기", style=discord.ButtonStyle.red, custom_id="report_button")
    async def report_Btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        # await interaction.response.send_message("dfdf")
        guild = interaction.guild
        member = interaction.user
        admin = get(guild.roles, id=1246901498705875085)
        overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                admin: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                member: discord.PermissionOverwrite(read_messages=True, send_messages=True)
            }
        name = '────《 신고 》────'
        class reportModal(ui.Modal, title="문의 또는 신고하기"):
                    Why = ui.TextInput(
                        label="문의 또는 신고내용을 간략히 입력해주세요.",
                        style=discord.TextStyle.long,
                        placeholder="",
                        required=False
                    )
                    async def on_submit(self, interaction: Interaction):
                        print(f'문의내용 : {self.Why.value}')
                        category = discord.utils.get(guild.categories, name=name)

                        privateChannel = await interaction.guild.create_text_channel(f'{interaction.user}님의 문의 또는 신고', overwrites=overwrites, category=category)
                        await interaction.response.send_message(f'<#{privateChannel.id}>채널이 생성되었습니다.', ephemeral=True)

                        embed = discord.Embed(title="신고알림", description='　')
                        embed.add_field(name='　', value=f'{interaction.user.mention}님이 신고채널을 생성하셨습니다.', inline=False)
                        embed.add_field(name='내용', value=f'{self.Why.value}', inline=False)

                        await privateChannel.send(f'{interaction.user.mention} <@&1246901498705875085>', embed=embed)
        await interaction.response.send_modal(reportModal())
        