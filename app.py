import discord, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv('TOKEN')


class Client(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=".",
            intents=discord.Intents.all(),
            enable_debug_events=True,
        )
        self.synced = False
        self.initial_extensions = []
        self.bot = commands.Bot

        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'cogs')

        for ext in os.listdir(path):
            if ext.endswith('.py'):
                filename = ext.split('.')[0]
                cog = f'cogs.{filename}'
                self.initial_extensions.append(cog)
                print(f'FOUND : {cog}')

    async def setup_hook(self):
        try:
            for ext in self.initial_extensions:
                if not self.extensions.get(ext):  # Cog가 이미 로드된 상태인지 확인
                    await self.load_extension(ext)
                    print(f"LOAD : {ext}")
                else:
                    print(f"{ext} is already loaded.")
            if not self.synced:
                await bot.tree.sync()
                self.synced = True
        
        except Exception as e:
            print(e)

        btn = self.get_cog("verifycation")
        self.add_view(btn.get_btn())
        self.add_view(btn.get_btn2())
        self.add_view(btn.get_btn3())

    async def on_ready(self):
        print("login")
        print("==============================\n")
        print(self.user.name)
        print(self.user.id)
        print("\n==============================")
        # logger.info("Bot Start")

    async def on_message(self, message):
        if message.author.bot:
            return None

        await bot.change_presence(activity=discord.Game(name="서버관리"))

        if (message.content.startswith("$로드") and message.author.guild_permissions.administrator):
            filename = message.content.replace("$로드", "").replace(" ", "")
            cog = f"cogs.{filename}"
            try:
                await self.load_extension(cog)
                await message.channel.send(f"{filename}.py가 로드 되었습니다.")
            except commands.errors.ExtensionAlreadyLoaded:
                await message.channel.send(f"{filename}.py는 이미 로드되었습니다.")
        elif (message.content.startswith("$언로드") and message.author.guild_permissions.administrator):
            filename = message.content.replace("$언로드", "").replace(" ", "")
            await self.unload_extension(f"cogs.{filename}")
            await message.channel.send(f"{filename}.py가 언로드 되었습니다.")
        
        elif message.content.startswith("$리로드"):
            filename = message.content.replace("$리로드", "").replace(" ", "")
            cog = f"cogs.{filename}"
            await self.unload_extension(cog)
            await self.load_extension(cog)
            await message.channel.send(f"{filename}.py가 리로드 되었습니다.")
        
        elif message.content.startswith("$cls"):
            os.system("cls")

bot = Client()
bot.run(bot_token)