import os
import discord
TOKEN = 'NzM1OTU2NDQxNDk5Njk3Mjgz.Xxn2TQ.SsXldPG5pKwYCN9t0GTnw9YOb48'



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
    if message.content == '0':
        await message.channel.send('fred es gay')


client.run(TOKEN)


