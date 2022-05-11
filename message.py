from abc import abstractclassmethod
import random
from time import strftime, localtime
from settings import PREFIX

class MessageHandler():
    '''
    parent class for message handling
    it controls all the channels flux
    '''
    def __init__(self, message):
        self.message = message

    async def handler(self):
        if self.message.channel.name == "discord-bot":
            await DiscordBot(self.message).send_message()
        elif self.message.channel.name == "calendar":
            await Calendar(self.message).send_message()

    @abstractclassmethod
    async def send_message(self):
        pass

class DiscordBot(MessageHandler):
    '''
    message handler for discord-bot channel interactions
    based on general/testing user inputs
    '''
    def __init__(self, message):
        super().__init__(message)

    async def send_message(self):
        username = str(self.message.author).split('#')[0]
        user_message = str(self.message.content)
        channel = str(self.message.channel.name)
        print(f'{username}: {user_message} ({channel})')

        if user_message.lower().startswith('hola'):
            await self.message.channel.send(f'Hola {username}!')
            return
        elif user_message.lower().startswith('chao'):
            await self.message.channel.send(f'Nos vemos pronto {username}!')
            return
        elif user_message.lower() == f'{PREFIX}random':
            response = f'This is your random number: {random.randint(1, 1000)}'
            await self.message.channel.send(response)
            return

        if user_message.lower() == f'{PREFIX}anywhere':
            await self.message.channel.send(f'This can be used anywhere!')
            return

class Calendar(MessageHandler):
    '''
    message handler for calendar channel interactions
    also ment to create new events and notificate stuff to admin user
    '''
    def __init__(self, message):
        super().__init__(message)

    async def send_message(self):
        username = str(self.message.author).split('#')[0]
        user_message = str(self.message.content)
        channel = str(self.message.channel.name)
        print(f'{username}: {user_message} ({channel})')

        if user_message.lower() == f'{PREFIX}time':
            await self.current_time()
            return

    async def current_time(self):
        response = strftime("%a, %d %b %Y %H:%M:%S", localtime())
        print(f'HORA ACTUAL: {response}')
        await self.message.channel.send(response)
        return
    