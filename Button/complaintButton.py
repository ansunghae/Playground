import discord
from discord import Intents, Game, Status, Object, ButtonStyle, app_commands, ui, Interaction, Message, User, PartialEmoji, SelectOption, CategoryChannel, PermissionOverwrite, permissions
from discord.ui import Button, View, Select, Modal, TextInput
from discord.ext import commands
from discord.utils import get

class complaints_button(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="문의하기", style=discord.ButtonStyle.blurple, custom_id="complaints_button")
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
        category = discord.utils.get(guild.categories, name=name)
        privateChannel = await interaction.guild.create_text_channel(f'{interaction.user}님의 문의', overwrites=overwrites, category=category)
        await interaction.response.send_message(f'<#{privateChannel.id}>채널이 생성되었습니다.', ephemeral=True)

        embed = discord.Embed(title="문의알림", description='　')
        embed.add_field(name='　', value=f'{interaction.user.mention}님이 문의채널을 생성하셨습니다.')
        await privateChannel.send(f'{interaction.user.mention} <@&1246901498705875085>', embed=embed)
