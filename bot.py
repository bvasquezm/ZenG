from discord.ext.commands import Bot
from message import MessageHandler

class ZenG(Bot):
    def __init__(self, prefix, *args, **kwargs):
        super().__init__(prefix, *args, **kwargs)
        self.prefix = prefix
        self.handle_message = None

    async def on_ready(self):
        print(f'We have logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        self.handle_message = MessageHandler(message)
        await self.handle_message.handler()