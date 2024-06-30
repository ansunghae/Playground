import discord, os
from discord.ext import commands
from discord import Interaction, ui

from Button.roleButton import voice_room
from Button.reportButton import report_button
from Button.verifyButton import verify_button

class verifycation(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    def get_btn(self):
        return voice_room()
    
    def get_btn2(self):
        return report_button()
    
    def get_btn3(self):
        return verify_button()
    
    # @discord.app_commands.command(name="가입버튼_생성", description="카지노 봇을 사용하기 위해 로그인을 해야 합니다.")
    # async def voiceRoom(self, interaction: Interaction):
    #     if (interaction.user.guild_permissions.administrator):
    #         await interaction.channel.send(
    #             view=voice_room(),
    #             embed=discord.Embed(
    #                 title="역할받기",
    #                 description="통화방 멘션알림을 받으시려면 아래 버튼을 눌러주세요",
    #                 color=0x1EFF00,
    #             ).set_footer(text="이미 역할이 있는경우 역할이 제거됩니다."),
    #         )
    #     else:
    #         await interaction.response.send_message("권한이 없습니다.", ephemeral=True)

    # @discord.app_commands.command(name="가입버튼_생성", description="자기소개버튼")
    # async def report(self, interaction: Interaction):
    #     if (interaction.user.guild_permissions.administrator):
    #         await interaction.channel.send(
    #             view=verify_button(),
    #             embed=discord.Embed(
    #                 title="자기소개 작성하기",
    #                 description="자기소개를 작성해서 서버의 모든것을 즐겨보세요!",
    #                 color=0x1EFF00,
    #             )
    #         )
    #     else:
    #         await interaction.response.send_message("권한이 없습니다.", ephemeral=True)

    @discord.app_commands.command(name="인증", description="놀이터서버에서 활동하기위한 인증을 하는 기능입니다.")
    async def verifycation_command(self, interaction: Interaction):
        if not interaction.user.get_role(963749174053052456):
            if interaction.channel_id == 972334185677221898:
                class VerifyModal(ui.Modal, title="인증하기"):
                    WhereJoin = ui.TextInput(
                        label="입장경로를 적어주세요 (필수X)",
                        style=discord.TextStyle.short,
                        placeholder="디스보드, 디코올, 타서버홍보 등",
                        required=False
                    )
                    ok = ui.TextInput(
                        label="규칙을 모두 읽으셨으면, '동의합니다' 를 입력하세요",
                        style=discord.TextStyle.short,
                        placeholder="동의합니다"
                    )
                    async def on_submit(self, interaction: Interaction):
                        if self.ok.value == '동의합니다':
                            verifyEmbed = discord.Embed(title="인증완료",description='　', color=0x00ff00)
                            verifyEmbed.add_field(name='　', value="인증이 완료되었습니다.\n역할이 자동으로 지급됩니다.")
                            await interaction.response.send_message(embed=verifyEmbed, ephemeral=True)
                            await interaction.user.add_roles(interaction.guild.get_role(963749174053052456))

                            verifyLogEmbed = discord.Embed(title="인증알림", description='　')
                            verifyLogEmbed.add_field(name='　', value=f'{interaction.user.mention}님이 인증을 완료하셨습니다.', inline=False)
                            verifyLogEmbed.add_field(name='　', value=f'입장경로 : {self.WhereJoin.value}', inline=False)
                            await interaction.guild.get_channel(986194109318438962).send(embed=verifyLogEmbed)
        
                        else:
                            verifyEmbed = discord.Embed(title="인증실패",description='　', color=0xff0000)
                            verifyEmbed.add_field(name='　', value="인증을 실패했습니다.\n인증을 다시 진행해주세요.")
                            await interaction.response.send_message(embed=verifyEmbed, ephemeral=True)
                await interaction.response.send_modal(VerifyModal())
        
            else:
                errorEmbed = discord.Embed(title="에러",description='　', color=0xff0000)
                errorEmbed.add_field(name='　', value="채널이 올바르지 않습니다.")
                await interaction.response.send_message(embed=errorEmbed, ephemeral=True)
        
        else:
            errorEmbed = discord.Embed(title="에러",description='　', color=0xff0000)
            errorEmbed.add_field(name='　', value="이미 인증이 되어있습니다.")
            await interaction.response.send_message(embed=errorEmbed, ephemeral=True)
                

async def setup(client: commands.Bot):
    await client.add_cog(verifycation(client))