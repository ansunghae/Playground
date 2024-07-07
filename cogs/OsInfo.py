import psutil
from datetime import datetime
import discord
from discord.ext import commands, tasks
import platform

class SystemInfo(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @discord.app_commands.command(name="정보", description="봇 정보와 상태를 확인합니다.")
    async def osinfo(self, interaction: discord.Interaction):
        if interaction.user.guild_permissions.administrator:
            await self.send_system_info(interaction)
        else:
            await interaction.response.send_message("권한이 없습니다.", ephemeral=True)

    async def send_system_info(self, interaction: discord.Interaction):
        memory = psutil.virtual_memory()
        total_memory = memory.total / (1024 ** 3)  # GB로 변환
        used_memory = memory.used / (1024 ** 3)    # GB로 변환
        memory_percent = memory.percent

        disk = psutil.disk_usage('/')
        total_disk = disk.total / (1024 ** 3)  # GB로 변환
        used_disk = disk.used / (1024 ** 3)    # GB로 변환
        disk_percent = disk.percent

        boot_time_timestamp = psutil.boot_time()
        boot_time = datetime.fromtimestamp(boot_time_timestamp)
        uptime_seconds = (datetime.now() - boot_time).total_seconds()
        
        days, remainder = divmod(uptime_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        uptime_str = f"{int(days)}d {int(hours)}h {int(minutes)}m {int(seconds)}s"
        
        osEmbed = discord.Embed(title="System Information", description='　')
        osEmbed.add_field(name="OS", value=f'{platform.system()}')
        osEmbed.add_field(name="RAM", value=f'{used_memory:.1f}GB / {total_memory:.1f}GB\n{memory_percent}% 사용중')
        osEmbed.add_field(name="DISK", value=f'{used_disk:.1f}GB / {total_disk:.1f}GB\n{disk_percent}% 사용중')
        osEmbed.add_field(name="System Uptime", value=f'{uptime_str}')
        
        await interaction.response.send_message(embed=osEmbed)

async def setup(bot: commands.Bot):
    await bot.add_cog(SystemInfo(bot))
