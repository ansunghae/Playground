import discord
from discord import Intents, Game, Status, Object, ButtonStyle, app_commands, ui, Interaction, Message, User, PartialEmoji, SelectOption, CategoryChannel, PermissionOverwrite
from discord.ui import Button, View, Select, Modal, TextInput

class voice_room(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="통화방 알림역할 받기", style=discord.ButtonStyle.green, custom_id="voice_room_getrole")
    async def voice_room_getroleBtn(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not interaction.user.get_role(973513733429141534):
            roleID = interaction.guild.get_role(973513733429141534)
            await interaction.user.add_roles(roleID)
            await interaction.response.send_message("역할을 받았습니다", ephemeral=True)
        else:
            roleID = interaction.guild.get_role(973513733429141534)
            await interaction.user.remove_roles(roleID)
            await interaction.response.send_message("역할을 제거했습니다", ephemeral=True)