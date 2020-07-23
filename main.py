import os
import discord
TOKEN = 'alavavergaagaaa'



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
client = MyClient()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '':
        await message.channel.send('fred es gay')


client.run(TOKEN)


